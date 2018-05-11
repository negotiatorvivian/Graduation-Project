#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import xgboost as xgb
import traceback
import random

from conf import predict_conf as PredictConf
import conf.mysql_conf as MysqlConf
import common.date_helper as DateHelper
import common.mysql_util as MysqlUtil

class RePredictWorker(object):
    """docstring for RePredictWorker"""
    def __init__(self, arg1, arg2):
        super(RePredictWorker, self).__init__()
        self.origin_data = pd.read_csv(arg1) 
        self.path = arg2
        self.mysql_statistic = MysqlUtil.Mysql(conf = MysqlConf.SHOPPING)
    
    def append_data(self):
        time = DateHelper.Date.get_timestamp()
        date = DateHelper.Date.round_day_stamp(time)
        sql = '''
            select 
                * 
            from 
                negative_samples
            where 
                create_time = %s and status = %s
        ''' % (date, MysqlConf.STATUS_VALID)
        res = self.mysql_statistic.fetchall(sql)
        if res is False or None:
            return False
        sample_list = []
        for item in res:
            row = [item['gender'], item['age'], item['occupation'], item['city'], item['years'], item['marital_status']]
            if len(item['prefer_cats']) == 0:
                return False
            cats = item['prefer_cats'].split(',')
            row.append(PredictConf.PROB)
            for cat in cats:
                res = [cat]
                res = res + row
                sample_list.append(res)
        if len(sample_list) == 0:
            return False
        data_class_list = np.array(sample_list)
        times = np.array([PredictConf.REPEAT_TIME]).repeat(len(sample_list))
        data_class_list = data_class_list.repeat(times, axis = 0)
        sample_list = pd.DataFrame(data_class_list, columns = PredictConf.LABEL)
        return sample_list

    def merge_samples(self, sample_list):
        sample = pd.concat([self.origin_data, sample_list], ignore_index = True)
        sample.fillna(999, inplace = True)    #填补缺失值
        target = sample.prob
        target = np.array(target) 
        sample = pd.DataFrame(sample, columns = PredictConf.LABEL)
        # print(sample[:10, :])
        sample.drop(['prob'], axis = 1, inplace = True)
        X = np.array(sample)
        random.shuffle(X)

        encoded_x = None
        for i in range(0, X.shape[1]):
            label_encoder = preprocessing.LabelEncoder()
            feature = label_encoder.fit_transform(X[:,i])
            feature = feature.reshape(X.shape[0], 1)
            onehot_encoder = preprocessing.OneHotEncoder(sparse = False)
            feature = onehot_encoder.fit_transform(feature)
            if encoded_x is None:
                encoded_x = feature
            else:
                encoded_x = np.concatenate((encoded_x, feature), axis = 1)
        
        sample = encoded_x.astype(int)  
        return sample, target


    def train_model(self, sample, target):
        params = list(PredictConf.PARAMS)
        length = int(sample.shape[0] * 0.8)
        print(length)
        X_train = sample[:length,:]
        y_lable = target[:length]
        X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_lable, 
                                                            test_size = 0.2)
        xgtrain = xgb.DMatrix(X_train,
                              label = y_train)
        xgcv = xgb.DMatrix(X_valid, label = y_valid)
        watchlist = [(xgtrain, 'train'),(xgcv,'eval')]
        model_1_xgboost = xgb.train(params, xgtrain, PredictConf.NUM_ROUNDS,
                                    evals = watchlist, early_stopping_rounds = 200, 
                                    verbose_eval = 100)

        model_1_xgboost.save_model(self.path + '/blackFri_1.model')
        model_1_xgboost.dump_model(self.path + '/blackFri_1.raw.txt')
        return True


    def run(self):
        try:
            res = self.append_data()
            if res is False:
                return False

            sample, target = self.merge_samples(res)
            if sample is False:
                return False

            self.train_model(sample, target)
            return True
        except:
            print(traceback.format_exc())
            return False





