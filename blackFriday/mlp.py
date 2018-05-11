##coding: UTF-8
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor
import random

df_train = pd.read_csv('cat.csv')

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

df_sample = pd.read_csv('Sample_Submission_Tm9Lura.csv')


frames = [df_train, df_test]
input = pd.concat(frames)
input.fillna(999, inplace=True)

target = input.prob
target = np.array(target)

input.drop(["Purchase","aver","prob"], axis=1, inplace=True)
input = input.applymap(str)
input_pd = input.copy()

input = np.array(input)

for i in range(input.shape[1]):
    lbl = preprocessing.LabelEncoder()
    lbl.fit(list(input[:,i]))
    input[:, i] = lbl.transform(input[:, i])

input = input.astype(int)

# fit
ss_x = preprocessing.StandardScaler()
train_x_disorder = ss_x.fit_transform(input[:df_train.shape[0],:])
test_x_disorder = ss_x.transform(input[df_train.shape[0]:,:])

ss_y = preprocessing.StandardScaler()
train_y_disorder = ss_y.fit_transform(target[:df_train.shape[0]].reshape(-1, 1))
test_y_disorder = ss_y.transform(target[df_train.shape[0]:].reshape(-1, 1))

# 多层感知器-回归模型 r^2 score 200-0.24,2000-.31,(7,30,30,20)2000-0.29
model_mlp = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(20, 20, 20), random_state=1,max_iter=2000)
model_mlp.fit(train_x_disorder,train_y_disorder.ravel())
mlp_score=model_mlp.score(test_x_disorder,test_y_disorder.ravel())
print('score',mlp_score)
