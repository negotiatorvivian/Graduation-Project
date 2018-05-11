from django.conf.urls import url, include
from django.contrib import admin
from recommendation.controller import rec_goods_controller as RecGoodsController

urlpatterns =[
    url(r'^rec_goods$', RecGoodsController.recommend_goods),
]