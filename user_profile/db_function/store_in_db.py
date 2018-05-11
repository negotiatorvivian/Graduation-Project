#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import settings
from common import date_helper as DateHelper
import common.mysql_util as MysqlUtil
import conf.mysql_conf as MysqlConf
import conf.business_conf as BusinessConf

class Storing(object):
    """docstring for Storing"""
    def __init__(self, arg):
        super(Storing, self).__init__()
        self.mysql_shopping = MysqlUtil.Mysql(conf = MysqlConf.SHOPPING)
        self.file = arg


    def read_data(self):
        file = open(self.file)
        if not file:
            return False
        categories = []
        while True:
            line = file.readline().strip('\n')
            if not line:
                break
            categories.append(line)

        file.close()
        res = self.store_data(categories)
        if res is False:
            return False
        return True



    def store_data(self, data_list):
        if len(data_list) == 0:
            return False
        create_date = DateHelper.Date.get_timestamp()
        date = DateHelper.Date.round_day_stamp(create_date)

        for index in range(len(data_list)):
            item_index = index/BusinessConf.CATEGORY_LEN + 1
            sql = '''
                insert into
                    categories(cat_id, cat_name, create_time, update_time)
                values(%s, "%s", %d, %d)
                ''' % (int(item_index), str(data_list[index]), create_date, date)
            res = self.mysql_shopping.write(sql)
            if res is False:
                return False

        return True


if __name__ == '__main__':   
    Storing(sys.argv[1]).read_data()       


