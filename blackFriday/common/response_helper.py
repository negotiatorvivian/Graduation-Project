#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from conf import errcode_conf as ErrorConf

class Response(object):
    
    @classmethod
    def success(cls, ret = {}, cors = True):
        body = json.dumps({'errorCode': 0, 'ret': ret}, ensure_ascii = False)
        response = HttpResponse(body)
        response['Content-Type'] = 'application/json; charset=utf-8'
        if cors == True:
            response['Access-Control-Allow-Origin'] = '*'
        return response

    # @classmethod
    # def fail(cls, module = 'DEFAULT', errcode = -10000, cors = True):
    #     config = getattr(ErrorConf, module)
    #     body = json.dumps({'errorCode': errcode, 'ret': config[errcode]}, ensure_ascii = False)
    #     response = HttpResponse(body)
    #     response['Content-Type'] = 'application/json; charset=utf-8'
    #     if cors == True:
    #         response['Access-Control-Allow-Origin'] = '*'
    #     return response


    @classmethod
    def fail(cls, module = 'DEFAULT', errcode = -10000, cors = True, errmsg = None):
        config = getattr(ErrorConf, module)
        errorMessage = config[errcode]
        if errmsg is not None:
            errorMessage = '服务器旅游去了'
        body = json.dumps({'errorCode': errcode, 'errorMessage': errorMessage}, ensure_ascii = False)
        response = HttpResponse(body)
        response['Content-Type'] = 'application/json; charset=utf-8'
        if cors == True:
            response['Access-Control-Allow-Origin'] = '*'
        return response