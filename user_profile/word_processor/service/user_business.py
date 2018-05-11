#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol

class UserBusiness(MRJob):
    """docstring for UserBusiness"""
    INPUT_PROTOCOL = JSONValueProtocol


    def mapper(self, _, data):
        if "business_id" in data:
            yield data['user_id'], data['business_id']

        elif "user_id" in data:
            yield data['user_id'], ''


    def combiner(self, user_id, business_id):
        business_ids = list()
        for buz_id in business_id:
            if buz_id == '':
                pass
            else:
                business_ids.append(buz_id)


        yield user_id, business_ids



    def ruducer(self, user_id, business_id):
        business_ids = list()
        for buz_id in business_id:
            if buz_id == '':
                pass
            else:
                business_ids.append(buz_id)


        yield user_id, business_ids


if __name__ == "__main__":
    UserBusiness().run()