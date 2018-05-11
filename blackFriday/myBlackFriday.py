# coding: utf-8

import pandas as pd
import numpy as np

import random
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn import linear_model



def TextProcessing(data_class_list, test_size=0.2):

    # 交叉检验
    random.shuffle(data_class_list)
    index = int(len(data_class_list) * test_size)
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]

    train_data = train_list[:,0:7]
    train_class = train_list[:,7]
    test_data = test_list[:,0:7]
    test_class = test_list[:,7]
    return train_data, train_class, test_data, test_class

if __name__ == '__main__':
    df = pd.read_csv('cat.csv')
    df_old = df

    df.drop(["Purchase","aver","User_ID"], axis=1, inplace=True)
    number = LabelEncoder()
    df['Gender'] = number.fit_transform(df['Gender'].astype(str))
    df['Age'] = number.fit_transform(df['Age'].astype(str))
    df['City_Category'] = number.fit_transform(df['City_Category'].astype(str))
    df['Stay_In_Current_City_Years'] = \
        number.fit_transform(df['Stay_In_Current_City_Years'].astype(str))

    # for i in range(0,df.columns.size-2):
    #     df.iloc[:,i] = number.fit_transform(df.iloc[:,i].astype(str))

    # http://www.terrylmay.com/2017/03/06/multiple-linear-regression/

    train_x=[]
    train_y=[]
    test_x = []
    test_y = []

    df_array = np.array(df)

    train_x, train_y, test_x, test_y = TextProcessing(df_array, test_size=0.2)


