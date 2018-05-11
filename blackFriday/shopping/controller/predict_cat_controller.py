#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import traceback
from shopping.service import predict_cat_service as PredictCatService
from common import response_helper as ResponseHelper


def predict_shopping(request):
    request = request.POST
    gender = request.get('gender', 'M')
    age = request.get('age')
    occupation = request.get('occupation')
    city_category = request.get('city', 'B')
    years = request.get('years')
    marital_status = request.get('marital_status')
    res = PredictCatService.add_user(gender, age, occupation, city_category, years, marital_status)
    if res is False:
        return ResponseHelper.Response.fail(module = 'PREDICT_SHOPPING', errcode = -11002)
    uid = res
    res = PredictCatService.predict_shopping(uid, gender, age, occupation, city_category, years, marital_status)
    if res is None:
        return ResponseHelper.Response.fail(module = 'PREDICT_SHOPPING', errcode = -11000)
    if res is False:
        print(traceback.format_exc())
        return ResponseHelper.Response.fail(module = 'PREDICT_SHOPPING', errcode = -11001)
    return ResponseHelper.Response.success(ret = res)


def modify_model(request):
    request = request.POST
    gender = request.get('gender', 'M')
    age = request.get('age')
    occupation = request.get('occupation')
    city_category = request.get('city', 'B')
    years = request.get('years')
    marital_status = request.get('marital_status')
    categories = request.get('categories').split(',')