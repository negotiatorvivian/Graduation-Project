#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

n_samples = 120000000
n_features = 1000
n_components = 3
n_top_words = 10


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        # message = "Topic #%d: " % topic_idx
        message = ''
        message += ", ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()


# Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
# to filter out useless terms early on: the posts are stripped of headers,
# footers and quoted replies, and common English words, words occurring in
# only one document or in at least 95% of the documents are removed.

print("Loading dataset...")
d1 = ''
# doc = open('dataset/output0')
doc = open('temp')
docs = []
for index, line in enumerate(doc.readlines()):
    if line.split():
        docs.append(line)
doc.close()
doc_list = [item.strip('\n').split(' ') for item in docs]
# doc_list = doc_list[:10]
# dataset = [w1 for w1 in d1.split(' ')]
# data_samples = dic_list[:n_samples]

# Use tf-idf features for NMF.
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                   max_features=n_features,
                                   stop_words='english')
# Use tf (raw term count) features for LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(min_df=2,
                                max_features=n_features,
                                stop_words='english')

# ----------------------------pure nmf----------------------------
tfidf = tf_vectorizer.fit_transform(doc_list[0])
nmf = NMF(n_components=n_components, random_state=1,
          beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
          l1_ratio=.5).fit(tfidf)
print("\nTopics in NMF model (Frobenius norm):")
tfidf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(nmf, tfidf_feature_names, n_top_words)

exit(0)
# ----------------------------pure nmf----------------------------
for index in range(len(doc_list)):
    tfidf = tfidf_vectorizer.fit_transform(doc_list[index])
    # Fit the NMF model
    # print("Fitting the NMF model (Frobenius norm) with tf-idf features, "
    #       "n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))

    # nmf = NMF(n_components=n_components, random_state=1,
    #           alpha=.1, l1_ratio=.5).fit(tfidf)

    # print("\nTopics in NMF model (Frobenius norm):")
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # print_top_words(nmf, tfidf_feature_names, n_top_words)

    # Fit the NMF model
    # print("Fitting the NMF model (generalized Kullback-Leibler divergence) with "
    #       "tf-idf features, n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))
    print(index)
    nmf = NMF(n_components=n_components, random_state=1,
              beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
              l1_ratio=.5).fit(tfidf)

    # print("\nTopics in NMF model (generalized Kullback-Leibler divergence):")
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names, n_top_words)
    
    tf = tf_vectorizer.fit_transform(doc_list[index])
    # tf = tf_vectorizer.fit_transform(doc_list[index])
    lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)

    lda.fit(tf)
    # print("\nTopics in LDA model:")
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)






# print("Fitting LDA models with tf features, "
#       "n_samples=%d and n_features=%d..."
#       % (n_samples, n_features))



