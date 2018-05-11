##coding: UTF-8
import pandas as pd
import numpy as np
from sklearn import preprocessing
import xgboost as xgb
import random
from xgboost import XGBClassifier

def calAverage(df_train):
    for i in range(1,20+1):
        aver = df_train.loc[df_train["cat"] == i].Purchase.mean()
        aver=round(aver,4)
        df_train.loc[df_train["cat"] == i,'aver']=aver
    df_train['prob']=df_train['Purchase']/df_train['aver']
    df_train.round({'prob':3})
    return df_train

df_train = pd.read_csv('cat1.csv') 
print('read over')
df_train.fillna(999, inplace=True)
# sklearn中的随机抽取
# train_x_disorder, test_x_disorder, train_y_disorder, test_y_disorder = train_test_split(x, y,  train_size=0.8, random_state=33)
data_class_list = np.array(df_train)
random.shuffle(data_class_list)
index = int(len(df_train) * 0.2)
train_list = data_class_list[index:]
test_list = data_class_list[:index]
df_train = pd.DataFrame(train_list,columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob'])
df_test = pd.DataFrame(test_list,columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob'])
print('read over')

df_train=calAverage(df_train)
df_test=calAverage(df_test)

# df_sample = pd.read_csv('Sample_Submission_Tm9Lura.csv')
# print('read over')
frames = [df_train, df_test]
input = pd.concat(frames)
# input.to_csv('data/output')
# exit(0)
input.fillna(999, inplace=True)    #填补缺失值

target = input.prob
target = np.array(target)   #将列‘prob’列为一个序列
input.drop(["User_ID", "Purchase","aver"], axis=1, inplace=True)

input.drop(["prob"], axis=1, inplace=True)

input = input.applymap(str)   #对input中每一个元素做字符串处理
input_pd = input.copy()
# print(input_pd.columns)
X = np.array(input)
print('read over')

encoded_x = None
for i in range(0, X.shape[1]):
    label_encoder = preprocessing.LabelEncoder()
    feature = label_encoder.fit_transform(X[:,i])
    feature = feature.reshape(X.shape[0], 1)
    onehot_encoder = preprocessing.OneHotEncoder(sparse = False)
    feature = onehot_encoder.fit_transform(feature)
    # features.append(feature)
    if encoded_x is None:
        encoded_x = feature
    else:
        encoded_x = np.concatenate((encoded_x, feature), axis = 1)
input = encoded_x.astype(int)   #标签数字化
# output = xgb.DMatrix(input, label = ['cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob'])
# output.save_binary(fname = 'data/binary_data')
# exit(0)
params = {}
params["min_child_weight"] = 10
params["subsample"] = 0.7
params["colsample_bytree"] = 0.7
params["scale_pos_weight"] = 0.8
params["silent"] = 1
params["max_depth"] = 6
params["nthread"] = 6
#params["gamma"] = 1
params["objective"] = "reg:linear"
params["eta"] = 0.1
# params["base_score"] = 1800
params["eval_metric"] = "rmse"
params["seed"] = 0

plst = list(params.items())
num_rounds = 1000


# -------------------------------------train------------------------------------
X_train = input[:df_train.shape[0],:]
y_lable = target[:df_train.shape[0]]
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_lable, test_size=0.2)
xgtrain = xgb.DMatrix(X_train,
                      label=y_train)
xgcv = xgb.DMatrix(X_valid, label = y_valid)
watchlist = [(xgtrain, 'train'),(xgcv,'eval')]
model_1_xgboost = xgb.train(plst, xgtrain, num_rounds,evals = watchlist,early_stopping_rounds=200,verbose_eval = 100)

model_1_xgboost.save_model('models/blackFri_1.model')
model_1_xgboost.dump_model('models/blackFri_1.raw.txt')


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
