##coding: UTF-8
import pandas as pd
import numpy as np
from sklearn import preprocessing
import xgboost as xgb
import random
from xgboost import XGBClassifier
# !!!wrong model
def calAverage(df_train):
    for i in range(1, 21):
        aver = df_train.loc[df_train["cat"] == i, 'Purchase'].mean()
        aver = round(aver, 4)
        df_train.loc[df_train["cat"] == i,'aver'] = aver
    df_train['prob'] = df_train['Purchase'] / df_train['aver']
    return df_train


def create_feature_map(features):
    outfile = open('models/featmap.txt', 'w')
    i = 0
    for feat in features:
        outfile.write('f{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close()


params = {}
# params["min_child_weight"] = 10
params["subsample"] = 0.7
# params["subsample"] = 0.5
params["colsample_bytree"] = 0.7
# params["scale_pos_weight"] = 0.8
params["silent"] = 1
params["max_depth"] = 6
# params["nthread"] = 6
#params["gamma"] = 1
# params["objective"] = "reg:linear"
params['objective'] = 'multi:softmax'
params["eta"] = 0.3
# params["base_score"] = 0.5
# params["eval_metric"] = "rmse"
params["eval_metric"] = "mloglossmerror"
params["eval_metric"] = "merror"

params["seed"] = 0
params['num_class'] = 20
plst = list(params.items())


# ---------------------------------------- begin here ----------------------------------------
df_train = pd.read_csv('data/cat_train.csv')
df_train.fillna(999, inplace=True)

df_test = pd.read_csv('data/cat_test.csv')
df_train.fillna(999, inplace=True)
# sklearn中的随机抽取
# train_x_disorder, test_x_disorder, train_y_disorder, test_y_disorder = train_test_split(x, y,  train_size=0.8, random_state=33)
data_class_list1 = np.array(df_train)
data_class_list2 = np.array(df_test)
random.shuffle(data_class_list1)
random.shuffle(data_class_list2)
df_train = pd.DataFrame(data_class_list1, columns=['Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob', 'cat1'])
df_test = pd.DataFrame(data_class_list2, columns=['Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob', 'cat1'])


frames = [df_train, df_test]
input = pd.concat(frames)

target = input.cat1
target = np.array(target)   #将列‘prob’列为一个序列
label_encoder = preprocessing.LabelEncoder()
label_encoder = label_encoder.fit(target)
label_encoded_y = label_encoder.transform(target)
# print(label_encoded_y, len(label_encoded_y))
input.drop(["cat1"], axis = 1, inplace = True)
# input.drop(["User_ID", "Purchase", "aver", "prob1", "prob"], axis=1, inplace=True)

# input = input.applymap(str)   #对input中每一个元素做字符串处理
# input_pd = input.copy()
X = np.array(input)
X = X.astype(str)
# for i in range(input.shape[1]):   #返回矩阵长度
#     lbl = preprocessing.LabelEncoder()
#     lbl.fit(list(input[:,i]))  #编码
#     input[:, i] = lbl.transform(input[:, i])   #将文字转换为数字形式
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
# X = encoded_x.astype(int)   #标签数字化

# print(encoded_x[:10])
# X_train = input[:df_train.shape[0],:]
# y_lable = target[:df_train.shape[0]]
from sklearn.model_selection import train_test_split
'''
随机划分训练集和测试集
'''
# X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_lable, test_size = 0.2)   
X_train, X_valid, y_train, y_valid = train_test_split(encoded_x, label_encoded_y, test_size = 0.2) 
model = xgb.XGBClassifier()
model.fit(X_train, y_train)
print(model) 

exit(0)
xgtrain = xgb.DMatrix(X_train, label = y_train)
xgcv = xgb.DMatrix(X_valid, label = y_valid)
watchlist = [(xgtrain, 'train'),(xgcv,'eval')]
model_1_xgboost = xgb.train(plst, xgtrain, num_boost_round = 10000, evals = watchlist, early_stopping_rounds = 20, verbose_eval = 100)
model_1_xgboost.save_model('models/blackFri_2.model')
model_1_xgboost.dump_model('models/blackFri_2.raw.txt')















# -------------------old code------------------------
# model_1_xgboost.dump_model('models/blackFri_1.nice.txt', 'models/featmap1.txt')

# bst = xgb.Booster(model_file = 'models/blackFri_1.model')
# pre = bst.predict(xgcv, pred_leaf=True)
# idx = X_valid[:,0]
# res  = [ ( int(idx[i]), pre[i] ) for i in range(len(pre)) ]
# print(res)


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
