#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import gensim
import math
from gensim import corpora, models, similarities
from collections import defaultdict

def cos(vector1,vector2):  
    dot_product = 0.0;  
    normA = 0.0;  
    normB = 0.0;  
    for a,b in zip(vector1,vector2):  
        dot_product += a*b  
        normA += a**2  
        normB += b**2  
    if normA == 0.0 or normB==0.0:  
        return None  
    else: 
        x = round(dot_product / ((normA*normB)**0.5), 3)
        return math.exp(0-x)  


frequency = defaultdict(int)
raw_data = ''
f = open('temp1')
for index, line in enumerate(f.readlines()):   
    if line.split():
        line = line.strip('\n')
        raw_data += line
f.close

raw_file = ''
f = open('temp')
for index, line in enumerate(f.readlines()):
    if index > 1 :   
        if line.split():
            line = line.strip('\n')
            raw_file += line
f.close
docs = [raw_data, raw_file]
print(raw_data)

# raw_data = raw_data.split(' ')[30:60]
raw_data = raw_data.split(' ')[:30]


raw_file = raw_file.split(' ')
for token in raw_file:
    frequency[token] += 1

# for token in raw_data:
#     frequency[token] += 1


output = ''
all_sum = float(0)
for token in raw_data:
    output += str(round(float(frequency[token])/float(len(raw_file)), 4)) + ', '
    all_sum += round(float(frequency[token])/float(len(raw_file)), 4)
print(output)
print(all_sum)


# --------------------useless--------------------
# dictionary = corpora.Dictionary([raw_file])
# corpus = [dictionary.doc2bow(text) for text in [raw_file]]
# tfidf = models.TfidfModel(corpus)

# new_vec = dictionary.doc2bow(raw_data)
# num = len(dictionary.token2id.keys())
# index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = num)
# sim = index[tfidf[new_vec]]
# print(sim)
# --------------------useless--------------------

# doc1 = []
# doc2 = []
# doc3 = []
# doc4 = []
# doc5 = []
# for word in raw_data[:10]:
#     doc1.append(frequency[word])

# for word in raw_data[10:20]:
#     doc2.append(frequency[word])

# for word in raw_data[20:30]:
#     doc3.append(frequency[word])

# for word in raw_data[30:40]:
#     doc4.append(frequency[word])

# for word in raw_data[40:50]:
#     doc5.append(frequency[word])


# print(cos(doc1, doc2), cos(doc1, doc3), cos(doc1, doc4), cos(doc1, doc5), 
#     cos(doc3, doc2),cos(doc2, doc4), cos(doc5, doc2), cos(doc3, doc4), cos(doc3, doc5), cos(doc4, doc5))


print(cos(doc1, doc2), cos(doc1, doc3), cos(doc2, doc3))




































