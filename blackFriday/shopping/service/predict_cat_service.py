#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn import preprocessing
import numpy as np
from conf import predict_conf as PredictConf
from conf import general_conf as GeneralConf
from shopping import models as ShoppingModel
from common import date_helper as DateHelper

def predict_shopping(gender, age, occupation, city_category, years, marital_status):
    list1 = []
    for i in range(PredictConf.CATEGORY_NUM):
        new_list = [i + 1, gender, age, occupation, city_category, years, marital_status]
        list1.extend(new_list)
    array_list = np.array(list1).reshape(PredictConf.CATEGORY_NUM, 7)
    data = pd.DataFrame(array_list, columns = PredictConf.LABEL)
    dataset = pd.read_csv('data/predict.csv')
    data_list = np.array(dataset)

    data_list = pd.DataFrame(data_list, columns = PredictConf.LABEL)
    sample_list = pd.concat([data, data_list], ignore_index = True)

    X = np.array(sample_list)
    X = X.astype(str)
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
    # sample_list = sample_list.astype(int)   #标签数字化
    encoded_x = encoded_x[:PredictConf.CATEGORY_NUM]
    modelfile = 'models/' + PredictConf.BLACK_FRI_MODEL + '.model'
    if not modelfile:
        return None
    bst = xgb.Booster(model_file = modelfile)
    # print(modelfile.__str__)
    bst_safe = bst.copy()
    data = xgb.DMatrix(encoded_x)
    xgb_pre = bst_safe.predict(data = data)
    # print(xgb_pre)
    res = {}
    for index in range(len(xgb_pre)):
        res[index] = xgb_pre[index]
    data = sorted(res.items(), key=lambda res: res[1], reverse = True)
    print(data)

    ret = []
    for item in data[:5]:
        ret.append(item[0] + 1)

    return ret


def add_user(gender, age, occupation, city_category, years, marital_status):
    if gender == 'M':
        user_gender = 0
    else:
        user_gender = 1
    if age == '0-17':
        user_age = 1
    elif age == '18-25':
        user_age = 2
    elif age == '26-35':
        user_age = 3
    elif age == '36-45':
        user_age = 4
    elif age == '46-55':
        user_age = 5
    else:
        user_age = 6
    res = ShoppingModel.ShoppingUsers.objects.filter(status = GeneralConf.STATUS_VALID)
    if res is False:
        return False
    count = len(res)
    user = {
        'nick_name' : 'Traverller_' + str(count),
        'password' : GeneralConf.DEFAULT_PASSWORD,
        'gender' : user_gender,
        'age' : user_age,
        'occupation' : occupation,
        'city' : city_category,
        'years' : years,
        'marital_status' : marital_status,
        'create_time' : DateHelper.Date.get_timestamp(),
        'update_time' : DateHelper.Date.get_timestamp()
    }
    res = ShoppingModel.ShoppingUsers.objects.create(**user)
    if res is False:
        return False
    return res.id


def add_negative_samples(gender, age, occupation, city_category, years, marital_status, categories):
    time = DateHelper.Date.get_timestamp()
    date = DateHelper.Date.round_day_stamp(time)
    sample = {
        'gender' : gender,
        'age' : age,
        'occupation' : occupation,
        'city' : city_category,
        'years' : years,
        'marital_status' : marital_status,
        'prefer_cats' : categories,
        'create_time' : date,
        'update_time' : date
    }
    res = ShoppingModel.NegativeSamples.objects.create(**sample)
    if res is False:
        return False
    return True


def check_diff(gender, age, occupation, city_category, years, marital_status, categories):
    rec_list = predict_shopping(gender, age, occupation, city_category, years, marital_status)
    rec_list = set(rec_list)
    if len(categories) == 0:
        return False
    categories = set(categories.strip(',').split(','))
    new_set = set()
    for item in categories:
        new_set.add(int(item))
    diff = new_set - rec_list
    if len(diff) == 0:
        return False
    ret = []
    for item in diff:
        ret.append(str(item))
    diff = ','.join(ret)
    return diff





