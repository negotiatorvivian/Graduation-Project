#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys


class MergeCategories(object):
    """docstring for MergeCategories"""
    def __init__(self, arg):
        super(MergeCategories, self).__init__()
        self.filename = arg


    def merge_categories(self):
        file = open(self.filename, 'r')
        if not file:
            return False
        categories = {}

        while True:
            line = file.readline().strip('\n')
            if not line:
                break
            business_id = line.split('\t')[0][1 : -1]
            temp = line.split('\t')[1][16 : -2]
            for item in temp.split(', '):
                key = item[1 : -1]
                # print(key)
                if key not in categories.keys():
                    # categories[key] = list()
                    categories[key] = [business_id]
                else:
                    categories[key].append(business_id)

        file.close()
        for key in categories.keys():
            print(key)




if __name__ == "__main__":
    MergeCategories(sys.argv[1]).merge_categories()





