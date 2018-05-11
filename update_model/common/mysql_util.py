#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import logging
import traceback
import MySQLdb
import conf.mysql_conf as MysqlConf


class Mysql(object):

    def __init__(self, conf = MysqlConf.SHOPPING):
        self.conf = conf
        # self.logger = logging.getLogger('standard')
        self.connect()


    def __del__(self):
        self.close()


    def connect(self, try_times = 3):
        for i in range(try_times):
            try:
                self.conn = MySQLdb.connect(host = self.conf['host'], port = self.conf['port'], user = self.conf['user'], passwd = self.conf['passwd'], db = self.conf['db'], charset = self.conf['charset'])
                self.conn.autocommit(1) 
                self.cursor = self.conn.cursor()
                return True
            except:
                print('%s\n%s' % ('mysql connect', traceback.format_exc()))
        return False


    def fetchone(self, sql, try_times = 3):
        for i in range(try_times):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchone()
                if res == None:
                    return None
                return dict(zip([desc[0] for desc in self.cursor.description], res))
            except:
                print('%s\n%s' % (sql, traceback.format_exc()))
                self.connect()
        return False


    def fetchall(self, sql, try_times = 3):
        for i in range(try_times):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                if len(res) == 0:
                    return []
                return [dict(zip([desc[0] for desc in self.cursor.description], row)) for row in res]
            except:
                print('%s\n%s' % (sql, traceback.format_exc()))
                self.connect()
        return False


    def write(self, sql, try_times = 3):
        for i in range(try_times):
            try:
                self.cursor.execute(sql)
                return True
            except:
                print('%s\n%s' % (sql, traceback.format_exc()))
                self.connect()
        return False


    def close(self):
        try:
            self.conn.close()
            return True
        except:
            print('%s\n%s' % ('mysql close', traceback.format_exc()))
        return False
