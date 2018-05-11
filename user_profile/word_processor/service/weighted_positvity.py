#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
import re

from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import RawValueProtocol, JSONValueProtocol
import jieba


def avg_and_total(iterable):
    """Compute the average over a numeric iterable."""
    items = 0
    total = 0.0

    for item in iterable:
        total += float(item)
        items += 1

    return total / items, total

MINIMUM_OCCURENCES = 10

MINIMUM_BUSINESSES = 3


class WeightedPositiveWords(MRJob):
    """Find the most positive words in the dataset."""

    # The input is the dataset - interpret each line as a single json
    # value (the key will be None)
    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol
    # INPUT_PROTOCOL = RawValueProtocol
    weight_list = []


        
    def mapper(self, _, data):
        if "review_id" in data:
            yield data['business_id'], ('review', (data['text'], data['stars'], data['useful']))

        elif "business_id" in data:
            if data['categories']:
                yield data['business_id'], ('categories', data['categories'])
        

    def reducer(self, business_id, reviews):
        reviews_list = []
        # word_list = []

        for data in reviews:
            if "review" in data:
                reviews_list.append(word.lower() for word in data[1][0])
                # weight_list.append(business_id + '$' + str(data[1][1]))
            else:
                pass
        # businesses = set()
        # norm = lambda word: re.sub('[^a-z]', '', word.lower())
        # for review in reviews:
        #     words = list(norm(word) for word in review[1][0].split())
        #     word_list += words
        #     businesses.add(business_id)
        #     positivities.append(review[1][1])

        # if len(businesses) < MINIMUM_BUSINESSES:
        #     return

        # avg, total = avg_and_total(positivities)
        # if total < MINIMUM_OCCURENCES:
        #     return
        # output = open("weight0.txt", "w+")
        # for item in weight_list:
        #     output.write(str(item) + '\n')
        # output.close()
        yield business_id, reviews_list



    # def review_mapper(self, category, biz_review_positivity):
    #     biz_id, review, positivity = biz_review_positivity

    #     yield category,(biz_id, positivity)


    # def positivity_reducer(self, category, biz_positivities):
    #     # os.removedirs("/Users/zhangziwei/user_profile/dataset/output/step/000")

    #     businesses = set()
    #     positivities = []
    #     for biz_id, positivity in biz_positivities:
    #         businesses.add(biz_id)
    #         positivities.append(positivity)

    #     if len(businesses) < MINIMUM_BUSINESSES:
    #         return

    #     avg, total = avg_and_total(positivities)

    #     if total < MINIMUM_OCCURENCES:
    #         return

    #     yield int(avg * 100), (category, total, businesses)


    # def steps(self):
    #     return MRStep(mapper = self.review_category_mapper, reducer = self.category_join_reducer)


if __name__ == "__main__":
    WeightedPositiveWords().run()