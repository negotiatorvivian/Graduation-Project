#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import settings
import random
from common import date_helper as DateHelper
import common.mysql_util as MysqlUtil
import conf.mysql_conf as MysqlConf
import conf.business_conf as BusinessConf
import conf.migaration_conf as MigarationConf

class Storing(object):
    """docstring for Storing"""
    def __init__(self):
        super(Storing, self).__init__()
        self.mysql_shopping = MysqlUtil.Mysql(conf = MysqlConf.SHOPPING)


    def read_data(self):
        sql = '''
            select *
                from
            shopping_goods
                where status = %s
            ''' % (MysqlConf.STATUS_VALID)
        res = self.mysql_shopping.fetchall(sql)
        if res is False:
            return False
        rows = []
        lats = self.random_numbers(MigarationConf.NORTH_LOC, MigarationConf.SOUTH_LOC, len(res))
        lons = self.random_numbers(MigarationConf.EAST_LOC, MigarationConf.WEST_LOC, len(res))

        for index in range(len(res)):
            row = res[index]
            data = {}
            data['trade_name'] = row['trade_name']
            data['description'] = row['description']
            data['category'] = row['category']
            data['price'] = row['price']
            data['features'] = row['features']
            data['score'] = row['score']
            data['latitude'] = (lats[index])
            data['longitude'] = lons[index]
            rows.append(data)

        res = self.store_data(rows)
        if res is False:
            return False
        return True



    def store_data(self, data_list):
        if len(data_list) == 0:
            return False
        create_date = DateHelper.Date.get_timestamp()
        # date = DateHelper.Date.round_day_stamp(create_date)

        for index in range(len(data_list)):
            sql = '''
                insert into
                    shopping_goods_test(trade_name, description, category, price, features, score, latitude, longitude, create_time, update_time)
                values("%s", "%s", %d, %d, "%s", %f, %f, %f, %d, %d)
                ''' % (data_list[index]['trade_name'], data_list[index]['description'], data_list[index]['category'], data_list[index]['price'], 
                data_list[index]['features'], data_list[index]['score'], data_list[index]['latitude'], data_list[index]['longitude'], create_date, create_date)
            res = self.mysql_shopping.write(sql)
            if res is False:
                return False

        return True


    def random_numbers(self, floor, ceiling, length):
        res = set()
        while len(res) < length:
            temp = round(random.uniform(floor, ceiling), 4)
            res.add(temp)
        return list(res)



if __name__ == '__main__':   
    Storing().read_data()       


