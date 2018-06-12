#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import xgboost as xgb
from xgboost import XGBRegressor

import pandas as pd
import numpy as np
from sklearn import preprocessing

def calAverage(df_train):
    average = []
    Purchase = []
    for i in range(1,20+1):
        aver = df_train.loc[df_train["cat"] == i].Purchase.mean()
        aver=round(aver,3)
        df_train.loc[df_train["cat"] == i,'aver']=aver
        average.append(aver)
    aver_sum = 0
    for i in range(1, 21):
        aver_sum += average[i - 1]
    print(aver_sum)
    for i in range(1000001, 1006041):
        person_sum = df_train.loc[df_train["User_ID"] == i].Purchase.sum()
        # print(person_sum)
        Purchase.append(person_sum)

    for index, row in df_train.iterrows():
        aver = average[int(row['cat']) - 1]
        weight = float(Purchase[int(row['User_ID']) - 1000001]) / float(aver_sum)
        row['prob'] = round(float(row['Purchase']) / float(weight) / float(aver), 3)

    df_train.round({'prob':3})
    return df_train


def cal_degree(df_train):
    degree = df_train['prob']/0.5 + 1
    df_train['degree'] = degree
    values = []
    for index, items in df_train.items():
        if index == 'degree':
            for value in items:
                value = int(value)
                if value < 7 and value >= 5:
                    value = 5
                elif value >= 7:
                    value = 6
                else:
                    pass 

                values.append(value)
    df_train['degree'] = values      
    return df_train


def one_hot_coding(train):
    # X = np.array(input)

    # encoded_x = None
    # for i in range(0, X.shape[1]):
    #     label_encoder = preprocessing.LabelEncoder()
    #     feature = label_encoder.fit_transform(X[:,i])
    #     feature = feature.reshape(X.shape[0], 1)
    #     onehot_encoder = preprocessing.OneHotEncoder(sparse = False)
    #     feature = onehot_encoder.fit_transform(feature)
    #     # features.append(feature)
    #     if encoded_x is None:
    #         encoded_x = feature
    #     else:
    #         encoded_x = np.concatenate((encoded_x, feature), axis = 1)

    # return encoded_x
    features = list(train.columns[1:])  #la colonne 0 est le quote_conversionflag 
    # print(features)
    for f in train.columns:
        if train[f].dtype=='object' and f != 'prob':
            lbl = preprocessing.LabelEncoder()
            lbl.fit(list(train[f].values))
            train[f] = lbl.transform(list(train[f].values))

    return train

def data_processing(train):
    xgb1 = XGBRegressor(
                     # num_class=6,
                     learning_rate =0.05,
                     n_estimators=1000,
                     max_depth=7,
                     missing=-999,
                     min_child_weight=3,
                     subsample=0.8,
                     colsample_bytree=0.8,
                     gamma=0,
                     reg_alpha = 0,
                     reg_lambda = 1,
                     objective= 'reg:linear',
                     nthread=4,
                     scale_pos_weight=1,
                     base_score = 0.5,
                     seed=0)
    predictors = [x for x in train.columns if x not in ['prob']]
    return xgb1, predictors

def split_dataset(df_train):
    index = int((df_train.shape[0]) * 0.8)
    data_class_list = df_train.values
    train_list = data_class_list[:index]
    test_list = data_class_list[index:]
    train_list = pd.DataFrame(train_list, columns=['cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob'])
    test_list = pd.DataFrame(test_list, columns=['cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob'])

    y_train = np.array(train_list.prob, dtype = 'float32')
    y_test = np.array(test_list.prob, dtype = 'float32')
    # print(train_list.shape[0], test_list.shape[0], len(y_train), len(y_test))
    return (train_list, y_train), (test_list, y_test)
