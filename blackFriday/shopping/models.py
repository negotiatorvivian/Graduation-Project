# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class ShoppingUsers(models.Model):
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    occupation = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    years = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, default = 0)
    update_time = models.IntegerField(blank=True, default = 0)
    status = models.IntegerField(blank=True, default = 1)

    class Meta:
        managed = False
        db_table = 'shopping_users'
