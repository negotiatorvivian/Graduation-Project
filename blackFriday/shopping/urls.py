from django.conf.urls import url, include
from django.contrib import admin
from shopping.controller import predict_cat_controller as PredictCatController

urlpatterns =[
    url(r'^predict_result$', PredictCatController.predict_shopping),
    url(r'^modify_model$', PredictCatController.modify_model),
]