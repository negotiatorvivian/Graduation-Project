#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import settings
from worker import re_predict_worker as RePredictWorker

class Main(object):

    def __init__(self):
        self.worker = RePredictWorker.RePredictWorker(sys.argv[1], sys.argv[2])


    def run(self):
        self.worker.run()


if __name__ == '__main__':   
    Main().run()