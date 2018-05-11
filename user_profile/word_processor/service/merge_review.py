#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import traceback
import sys
import jieba
import re

class MergeReview(object):
    """docstring for MergeReview"""
    def __init__(self, arg, arg1):
        super(MergeReview, self).__init__()
        self.filename = arg
        self.outputfile = arg1

    def mapper(self):
        try:
            file = open(self.filename)
            if not file:
                return False
            result_dict = dict()
            while True:
                res = file.readline().strip('\n')
                # print(res)
                if not res:
                    break
                key = res.split('\t')[1]
                # print(key)
                if key in result_dict:
                    value = res.split('\t')[2]
                    result_dict[key] += value[13 : -2].split('", ')[0].lower()
                else:
                    value = res.split('\t')[2]
                    result_dict[key] = value[13 : -2].split('", ')[0].lower()


            review_text = open(self.outputfile, 'w+')
            if not review_text:
                return False
            for item in result_dict.keys():
                review_text.write(item + ' ' + result_dict[item] + '\n')
            review_text.close()
            return True

        except:
            print(traceback.format_exc())
            return False

    def get_stop_words(self):
        file = open('dataset/stopwords.dic', 'r')
        stopwords = [line.strip() for line in file] 
        stopwords = set(stopwords)
        file.close()
        
        # 读数据集
        # file = open(self.filename,'r')
        # documents = [document.strip('\n') for document in file] 
        # file.close()
        pattern = '[a-z]+'

        doc = ''
        docs = []
        currentDocument = []
        currentWordId = 0
        file = open(self.outputfile, 'r')
        while True:
            res = file.readline().strip('\n')
            if not res:
                break
            res = res.split('"', 2)[2][1:]
            # res = re.sub('\\n+\\+', ' ',res)
            res = re.sub('\\n+', ' ', res)
            it = re.finditer(pattern, res)
            for match in it:
                content = match.group()
                if content not in stopwords and len(content) > 2:
                    doc += content + ' '
            docs.append(doc)
            doc = ''
    
        for item in docs:
            print(item)
        return True

    def run(self):
        self.mapper()
        self.get_stop_words()



if __name__ == "__main__":
    MergeReview(sys.argv[1], sys.argv[2]).run()
