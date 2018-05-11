#!/bin/bash
export LD_LIBRARY_PATH=/usr/local/lib

BASE_DIR=$(cd $(dirname "$0"); pwd)

/usr/local/bin/python3 master/re_predict_master.py /Users/zhangziwei/zzw/Graduation\ Project/blackFriday/data/output.csv /Users/zhangziwei/zzw/Graduation\ Project/blackFriday/models
echo 'done'