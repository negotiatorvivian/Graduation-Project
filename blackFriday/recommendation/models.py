# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    cat_id = models.IntegerField(blank=True, null=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, default = 0)
    update_time = models.IntegerField(blank=True, default = 0)
    status = models.IntegerField(blank=True, default = 1)

    class Meta:
        managed = False
        db_table = 'categories'


class ShoppingGoods(models.Model):
    trade_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    features = models.CharField(max_length=100, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, default = 0)
    update_time = models.IntegerField(blank=True, default = 0)
    status = models.IntegerField(blank=True, default = 1)

    class Meta:
        managed = False
        db_table = 'shopping_goods'


class ShoppingGoodsTest(models.Model):
    trade_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    features = models.CharField(max_length=100, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, default = 0)
    update_time = models.IntegerField(blank=True, default = 0)
    status = models.IntegerField(blank=True, default = 1)

    class Meta:
        managed = False
        db_table = 'shopping_goods_test'

