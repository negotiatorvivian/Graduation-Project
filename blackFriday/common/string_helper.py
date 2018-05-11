#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def string_capitalize(features):
    try:
        if features is None:
            return ''
        str_list = features.split(',')
        new_list = []
        for item in str_list:
            new_list.append(item.capitalize())
        features = ', '.join(new_list)
        return features
    except:
        return ''
