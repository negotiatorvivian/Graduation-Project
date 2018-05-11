#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import urllib.request
from gensim import corpora, models, similarities
import gensim
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

n_samples = 10000
n_features = 5000
# n_features = 500
n_components = 50
# n_components = 10
n_top_words = 20

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
# --------------read model-file--------------------
model_list = ''
f = open('dataset/out_pre')
for index, line in enumerate(f.readlines()):
    if line.split():
        model_list += line
f.close()
word_list = model_list.split(' ')
# word_list = word_list[:n_samples]


tf_vectorizer = CountVectorizer(min_df = 20, max_features = n_features, stop_words = 'english')
tf = tf_vectorizer.fit_transform(word_list)
print('begin lda')
lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)

lda.fit(tf)
print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

