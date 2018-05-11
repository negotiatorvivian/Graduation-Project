#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
import jieba
from gensim import corpora, models, similarities
import gensim
import re
'''
正则匹配
'''
pattern = '[，|？|“|”|。|：|、|；|(|)|《|》|（|）|\\n|—|\d|　｜！]+'


d1=""
d2=""
'''
读文件tt22,tt44
'''
f = open('dataset/tt22')
for index, line in enumerate(f.readlines()):
    if line.split():
        d1 += line
f.close
d1 = re.sub(pattern, '', d1)
data1 = jieba.cut(d1)
data11 = ' '.join(data1)

# f = open(r"C:\\Users\yjyyj\Desktop\tt7.txt")
f = open('dataset/tt44')
for index, line in enumerate(f.readlines()):   
    if line.split():
        d2 += line
f.close
d2 = re.sub(pattern, '', d2)
data2 = jieba.cut(d2)
data21 = ' '.join(data2)
'''
合并data11和data21
'''
docs = [data11,data21]
tall = [[w1 for w1 in doc.split(' ')]
        for doc in docs]
from collections import defaultdict
frequency = defaultdict(int)

stopfile = open('dataset/stopwords.dic')
if not stopfile:
    exit(1)
stopwords = []
while True:
    line = stopfile.readline().strip('\n')
    if not line:
        break
    stopwords.append(line)
stopfile.close()
'''
计算词频
当文件大时可以增大mdzz,视情况而定
'''
for text in tall:
    for token in text:
        if token not in stopwords:
            frequency[token] += 1
mdzz = 5
tall = [[token for token in text if frequency[token] > mdzz]
        for text in tall]
dictionary = corpora.Dictionary(tall)
while len(dictionary.token2id.keys()) > 500:
    mdzz += 5
    tall = [[token for token in text if frequency[token] > mdzz]
            for text in tall]
    dictionary = corpora.Dictionary(tall)
'''
读文件tt33
'''
thisnoveldata = ""
f = open("dataset/tt33")
for index, line in enumerate(f.readlines()):
    if line.split():
        thisnoveldata += line
f.close
thisnoveldata = re.sub(pattern, '', thisnoveldata)
data3 = jieba.cut(thisnoveldata)
data31 = ' '.join(data3)
data31_ = ''
for word in data31.split(' '):
    if word not in stopwords:
        data31_ += word + ' '
data31 = data31_
this_novel = data31
'''
构建tt3的词典new_vec和tt2&tt4的词典corpus
'''
new_vec = dictionary.doc2bow(this_novel.split(' '))
corpus = [dictionary.doc2bow(text) for text in tall]
tfidf = models.TfidfModel(corpus)
print(dictionary.token2id)
'''
计算相似性
'''
num = len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = num)
sim = index[tfidf[new_vec]]
print(sim)



