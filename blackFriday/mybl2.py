##coding: UTF-8
import pandas as pd
import numpy as np
from sklearn import preprocessing
import xgboost as xgb
import random
import train_cv as TrainCV
import cal_param as CalParam
# import matplotlib.pyplot as plt

# df_train = pd.read_csv('data/output.csv') 
df_train = pd.read_csv('cat2.csv') 
print('read over')

# data_class_list = np.array(df_train)
# random.shuffle(data_class_list)
# index = int(len(df_train) * 0.8)
# train_list = data_class_list[:index]
# test_list = data_class_list[index:]
# df_train = pd.DataFrame(train_list,columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob','degree'])
# df_test = pd.DataFrame(test_list,columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob','degree'])

# df_train=CalParam.calAverage(df_train)
# df_test=CalParam.calAverage(df_test)


# frames = [df_train, df_test]
# input = pd.concat(frames)

# df_train.to_csv('cat2.csv', index = False)
# exit(0)
input = pd.DataFrame(df_train, columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob','degree']) 
input.fillna(-999, inplace=True) 
input.drop(["User_ID", "Purchase","aver","degree"], axis=1, inplace=True)
input = input.applymap(str)   #对input中每一个元素做字符串处理
input_pd = input.copy()
# print(input_pd.columns)

encoded_x = CalParam.one_hot_coding(input_pd)
xgb1, predictors = CalParam.data_processing(encoded_x)
# TrainCV.modelfit(xgb1, encoded_x, predictors)
# TrainCV.train_cv(encoded_x, predictors)
# exit(0)
params = {}
params["min_child_weight"] = 10
params["scale_pos_weight"] = 1
params["gamma"] = 0
params["alpha"] = 0.7

params["max_depth"] = 6
params["subsample"] = 0.8
params["colsample_bytree"] = 0.8
params["silent"] = 1
# params["nthread"] = 6
params["objective"] = "reg:linear"
params["eta"] = 0.1
params["eval_metric"] = "rmse"
params["seed"] = 0

plst = list(params.items())
num_rounds = 5000


# -------------------------------------train------------------------------------
X_train = encoded_x[:df_train.shape[0],:]
# X_train = input[:df_train.shape[0],:]
y_lable = target[:df_train.shape[0]]
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_lable, test_size=0.2)
xgtrain = xgb.DMatrix(X_train,
                      label=y_train)
xgcv = xgb.DMatrix(X_valid, label = y_valid)
watchlist = [(xgtrain, 'train'),(xgcv,'eval')]
print('min_child_weight :' + str(params['min_child_weight']))
# print('subsample :' + str(params['subsample']))
print('gamma :' + str(params['gamma']))
print('scale_pos_weight :' + str(params['scale_pos_weight']))
print('alpha :' + str(params['alpha']))
model_1_xgboost = xgb.train(plst, xgtrain, num_rounds,evals = watchlist,early_stopping_rounds=200,verbose_eval = 200)

model_1_xgboost.save_model('models/blackFri_1.model')
model_1_xgboost.dump_model('models/blackFri_1.raw.txt')
# xgb.plot_importance(model_1_xgboost,importance_type = 'gain')
# xgb.plot_importance(model_1_xgboost,importance_type = 'weight')
# plt.show()


# -------------------------------------predict------------------------------------

# model_1_predict = model_1_xgboost.predict(xgb.DMatrix(input[df_train.shape[0]:,:]))
# model_1_predict[model_1_predict<0] = 0
# df_sample.prob = model_1_predict

# df_sample.orig = df_test.prob
# # df_sample.to_csv("mybltest.csv", index=False,float_format='%.3f')
# print('begin over')
# model = XGBClassifier(
#     learning_rate=0.1,
#     n_estimators=10000,
#     max_depth=10,
#     base_score=1800,
#     # updater= 'grow_gpu_hist',
#     # tree_method='exact',
#     min_child_weight=10,
#     gamma=1,
#     subsample=0.7,
#     colsample_bytree=0.7,
#     objective='reg:linear',
#     n_jobs=8,
#     scale_pos_weight=0.8,
#     random_state=1000,
#     # max_delta_step=5,
#     silent=1,
#     # reg_lambda=1,
# )
# model.fit(input[:df_train.shape[0],:],target[:df_train.shape[0]],eval_metric='rmse',eval_set=[(input[:df_train.shape[0],:],target[:df_train.shape[0]])])
# model._Booster.save_model('model/xgb_6_21_23.model')
# import matplotlib.pyplot as plt
# xgb.plot_importance(model_1_xgboost,importance_type='gain')
# xgb.plot_importance(model_1_xgboost,importance_type='weight')
# plt.show()
