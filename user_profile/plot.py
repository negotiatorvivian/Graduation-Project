#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np 
import pandas as pd
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt

def calAverage(df_train):
    for i in range(1,20+1):
        aver = df_train.loc[df_train["cat"] == i].Purchase.mean()
        aver=round(aver,4)
        df_train.loc[df_train["cat"] == i,'aver']=aver
    df_train['prob']=df_train['Purchase']/df_train['aver']
    df_train.round({'prob':3})

    return df_train

def group(d):
    malelist = []
    femalelist = []
    # dataframe = d.loc[d["Gender"] == 'F']
    for i in range(1, 21):  
        dataframe = d.loc[d["Gender"] == 'F']
        dataframe = pd.DataFrame(dataframe, columns = ['cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob'])
        temp = dataframe.loc[dataframe["prob"] > 1]
        column = np.array(temp.Gender)
        count1 = 0
        for item in column:
            if item == 'F':
                count1 += 1
        count2 = len(column) - count1
        malelist.append(count2)
        femalelist.append(count1)
    print(malelist)
    print(femalelist)
    return malelist, femalelist

def group1(d):
    agelist1 = []
    agelist2 = []
    agelist3 = []
    agelist4 = []
    agelist5 = []
    agelist6 = []
    agelist7 = []
    for i in range(1, 21):  
        dataframe = d.loc[d["cat"] == i]
        dataframe = pd.DataFrame(dataframe, columns = ['cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','prob'])
        temp = dataframe.loc[dataframe["prob"] > 1]
        column = np.array(temp.City_Category)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        for item in column:
            if item == 'A':
                count1 += 1
            elif item == 'B':
                count2 += 1
            elif item == 'C':
                count3 += 1
            elif item == '36-45':
                count4 += 1
            elif item == '46-50':
                count5 += 1
            elif item == '51-55':
                count6 += 1
            else:
                count7 += 1

        # count2 = len(column) - count1
        agelist1.append(count1)
        agelist2.append(count2)
        agelist3.append(count3)
        agelist4.append(count4)
        agelist5.append(count5)
        agelist6.append(count6)
        agelist7.append(count7)
    print(agelist1, agelist2, agelist3, agelist4, agelist5, agelist6, agelist7)
    return agelist1, agelist2, agelist3, agelist4, agelist5, agelist6, agelist7



dataset = pd.read_csv('/Users/zhangziwei/zzw/Graduation Project/blackFriday/cat1.csv')
dataset.fillna(999, inplace=True)
data_class_list = np.array(dataset)
df_train = pd.DataFrame(data_class_list,columns=['User_ID','cat','Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Purchase','aver','prob'])
df_train=calAverage(df_train)
df_train.drop(['User_ID', 'Purchase', 'aver'], axis = 1)
fig = plt.figure(figsize=(8, 6), dpi=80)
ax = plt.subplot(1, 1, 1)
N = 20
gender1, gender2 = group(df_train)
age1, age2, age3, age4, age5, age6, age7 = group1(df_train)
width = 0.8
# n_groups = 6
opacity = 0.4

index = np.arange(N + 1)
index1 = np.arange(1, N + 1)
x_lable = tuple(index)


x1 = [int(x) for x in range(1, 21)]
x2 = [int(x) for x in range(1, 21)]
y1 = gender1
y2 = gender2
# l1 = plt.bar(index1, age2, color='lavender', width = width, alpha=1)
# l2 = plt.bar(index1, age3, color='cornflowerblue', width= width, alpha=1)
# l3 = plt.bar(index1, age1, color='darkblue', width= width, alpha=1)
l3 = plt.bar(index + width, age1, width = width, alpha=1, color = '#312a94')
l4 = plt.bar(index + width, age2, width = width, alpha=1, color = '#3e4988')
l5 = plt.bar(index + width, age3, width = width, alpha=1, color = '#3099ff')
l6 = plt.bar(index + width, age4, width = width, alpha=1, color = '#00d7ff')
l7 = plt.bar(index + width, age5, width = width, alpha=1, color = '#00fcdf')
l8 = plt.bar(index + width, age6, width = width, alpha=1, color = '#16fbab')
l9 = plt.bar(index + width, age7, width = width, alpha=1, color = '#16fbab')
for x1,x2,x1, y1, y2,y3 in zip(x1,x2,x1, age1, age2, age3):
    plt.text(x1 , y1, '%.0f' % y1, ha='center', va='bottom')
    plt.text(x2 , y2, '%.0f' % y2, ha='center', va='bottom')
    plt.text(x2 , y3, '%.0f' % y3, ha='center', va='bottom')
# 显示
plt.title(u'City Influence', fontsize=20)
plt.xlabel(u'categories')
plt.ylabel(u'numbers')
ax.set_xticks(index - width/2)
ax.set_xticklabels(x_lable)
plt.legend(handles = [l3, l4, l5, l6, l7, l8, l9], labels = ['A', 'B', 'C'], loc = 'best')
# plt.legend(handles = [l1, l2, l3, l4, l5, l6, l7, l8, l9, ], labels = ['Male', 'Female'], loc = 'best')
plt.show()