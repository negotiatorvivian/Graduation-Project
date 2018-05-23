#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import traceback
from conf import general_conf as GeneralConf
from recommendation import models as RecommendModel
from conf import recommend_conf as RecommendConf
from common import string_helper as StringHelper

def get_demand_goods(res_list, append_list = None):
    res = RecommendModel.ShoppingGoodsTest.objects.filter(category__in = res_list, status = GeneralConf.STATUS_VALID).order_by('-score')
    if res is False or len(res) == 0:
        return False
    # print(len(res), res)
    ret = []
    for good in res:
        row = {}
        row['trade_name'] = good.trade_name
        row['description'] = good.description
        row['latitude'] = good.latitude
        row['longitude'] = good.longitude
        features = StringHelper.string_capitalize(good.features)
        if features is None:
            features = ''
        row['features'] = features
        row['score'] = float(good.score)
        row['category'] = good.category
        ret.append(row)
    # print(ret)
    if len(ret) > RecommendConf.DISPLAY_PIC_NUM:
        return ret
    res = RecommendModel.ShoppingGoodsTest.objects.filter(category__in = append_list, status = GeneralConf.STATUS_VALID).order_by('-score')
    for good in res:
        row = {}
        row['trade_name'] = good.trade_name
        row['description'] = good.description
        row['latitude'] = good.latitude
        row['longitude'] = good.longitude
        features = StringHelper.string_capitalize(good.features)
        if features is None:
            features = ''
        row['features'] = features
        row['score'] = float(good.score)
        row['category'] = good.category
        ret.append(row)
    ret = ret[:RecommendConf.DISPLAY_PIC_NUM] if len(ret) > RecommendConf.DISPLAY_PIC_NUM else ret
    return ret


def get_hot_goods(val = 3, cur_list = None):
    res = RecommendModel.Categories.objects.exclude(cat_id__in = cur_list, status = GeneralConf.STATUS_VALID).distinct().order_by('-clicks')[:val] 
    if res is None:
        return None
    ret = []
    for item in res:
        ret.append(int(item.cat_id))
    
    return ret
    


def add_click(rec_list):
    res = RecommendModel.Categories.objects.filter(cat_id__in = rec_list, status = GeneralConf.STATUS_VALID)
    for item in res:
        item.clicks += 1
        item.save()

    if res is None:
        return False
    return res


