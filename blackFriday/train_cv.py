#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
from sklearn.cross_validation import *
from sklearn import metrics   
from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV  
import cal_param as CalParam

# import matplotlib.pylab as plt
# from matplotlib.pylab import rcParams
# rcParams['figure.figsize'] = 12, 4


param_test1 = {
 'max_depth':list(range(5,7,1)),
 'min_child_weight':list(range(1,6,2))
}

def modelfit(alg, dtrain, predictors, useTrainCV = True, cv_folds = 3, early_stopping_rounds = 200):
    (X_train, y_train), (X_test, y_test) = CalParam.split_dataset(dtrain)

    y_label = np.ma.append(y_train.T, y_test.T)
    # .reshape(dtrain.shape(0), 1)
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        print(xgb_param)
        xgtrain = xgb.DMatrix(dtrain[predictors].values, label = y_label)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                        metrics='rmse', early_stopping_rounds=early_stopping_rounds, seed = 0, verbose_eval = 100, stratified = False)
        alg.set_params(n_estimators=cvresult.shape[0])
    print(cvresult.shape[0])
    # print(xgtrain.feature_types, dtrain[predictors].values[:10])
    alg.fit(X_train[predictors].values, y_train, eval_set=[(X_train[predictors].values, y_train), (X_test[predictors].values, y_test)], eval_metric='rmse', verbose=100)
      
    #Predict training set:
    dtrain_predictions = alg.predict(X_test[predictors].values)
     
    #Print model report:
    print( "\nModel Report")
    # print( "Accuracy : %.4g" % metrics.accuracy_score(y_test, dtrain_predictions))
    print( "explained_variance_score : %.4g" % metrics.explained_variance_score(y_test, dtrain_predictions, multioutput = 'uniform_average'))
    # feat_imp = pd.Series(alg.get_fscore()).sort_values(ascending=False)
    # feat_imp.plot(kind='bar', title='Feature Importances')
    # plt.ylabel('Feature Importance Score')


# ---------------------------------------------- version 1.0 ----------------------------------------------
def train_cv(dtrain, predictors):
    # xgb_model = xgb.XGBClassifier()
    # parameters = {'nthread':[6], #when use hyperthread, xgboost may become slower
    #               'objective':['reg:liner'],
    #               'learning_rate': [0.1], #so called `eta` value
    #               'max_depth': [6],
    #               'min_child_weight': [1],
    #               'silent': [1],
    #               'subsample': [0.8],
    #               'colsample_bytree': [0.8],
    #               'missing':[-999],
    #               'seed': [0],
    #               'n_estimators':[2000],
    #               'gamma' : [0],
    #               'scale_pos_weight' : [1]
    #               }
    (X_train, y_train), (X_test, y_test) = CalParam.split_dataset(dtrain)
    xgb1 = XGBRegressor(
                     learning_rate =0.05,
                     n_estimators=200,
                     max_depth=6,
                     min_child_weight=1,
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
    clf = GridSearchCV(xgb1, param_test1, n_jobs = 5, 
                       # cv = StratifiedKFold(label, n_folds = 5, shuffle = False), 
                       cv = 3,
                       scoring='r2',
                       verbose=1)
    # features = list(dtrain.columns[1:])
    y_label = np.ma.append(y_train.T, y_test.T)
    clf.fit(dtrain[predictors].values, y_label)
    best_parameters, score, _ = max(clf.grid_scores_, key=lambda x: x[1])
    print('Raw average_precision score:', score)
    for param_name in sorted(best_parameters.keys()):
        print("%s: %r" % (param_name, best_parameters[param_name]))






























