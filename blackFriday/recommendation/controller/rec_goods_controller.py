#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import traceback
from common import response_helper as ResponseHelper
from recommendation.service import rec_goods_service as RecGoodsService
from conf import recommend_conf as RecommendConf
def recommend_goods(request):
    request = request.POST
    num = int(request.get('num'))
    rec_list = []
    for i in range(num):
        param = 'cat' + str(i)
        rec_list.append(int(request.get(param)))

    # print(rec_list)
    if len(rec_list) == 0:
        res = RecGoodsService.get_hot_goods(val = RecommendConf.DISPLAY_PIC_NUM)
        if res is False:
            print(traceback.format_exc())
            return ResponseHelper.Response.fail(module = 'RECOMMEND_GOODS', errcode = -12001)
        else:
            return ResponseHelper.Response.success(ret = res)

    else:
        if len(rec_list) < RecommendConf.DISPLAY_PIC_NUM:
            res1 = RecGoodsService.get_hot_goods(val = RecommendConf.DISPLAY_PIC_NUM - len(rec_list), cur_list = rec_list)
            if res1 is None:
                pass
            else:
                rec_list.extend(res1)
            # print(rec_list)
        res = RecGoodsService.get_demand_goods(rec_list)
        if res is False:
            return ResponseHelper.Response.fail(module = 'RECOMMEND_GOODS', errcode = -12000)

        ret = RecGoodsService.add_click(rec_list)
        if ret is False:
            return ResponseHelper.Response.fail(module = 'RECOMMEND_GOODS', errcode = -12002)
        return ResponseHelper.Response.success(ret = res)
