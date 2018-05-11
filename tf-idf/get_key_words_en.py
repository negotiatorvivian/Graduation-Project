#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
# import jieba
from gensim import corpora, models
from nltk.stem.lancaster import LancasterStemmer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
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
st1 = LancasterStemmer()
f = open('/Users/zhangziwei/user_profile/output2')
for index, line in enumerate(f.readlines()):
    if line.split():
        d1 += line
f.close
docs = [w1 for w1 in d1.split(' ')]
# docs = [d1]
# # tall = [[st1.stem(w1) for w1 in doc.split(' ')]
# #         for doc in docs]
# tall = [[w1 for w1 in doc.split(' ')]
#         for doc in docs]
# from collections import defaultdict
# frequency = defaultdict(int)
# for text in tall:
#     for token in text:
#         frequency[token] += 1

# mdzz = 20
# tall = [[token for token in text if frequency[token] > mdzz]
#         for text in tall]

# dictionary = corpora.Dictionary(tall)
# while len(dictionary.token2id.keys()) > 100:
#     mdzz += 10
#     tall = [[token for token in text if frequency[token] > mdzz]
#             for text in tall]
#     dictionary = corpora.Dictionary(tall)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)
tfidf = transformer.fit_transform(X)
transformer = TfidfTransformer()  
print(tfidf.toarray())
# corpus = [dictionary.doc2bow(text) for text in tall]
# tfidf = models.TfidfModel(corpus)
# res = dictionary.token2id
# res = sorted(res.items(), key = lambda res: res[1], reverse = True)
# print(res)




