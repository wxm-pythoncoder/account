from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    money = models.IntegerField(verbose_name='金额',null=True)
    address = models.CharField(max_length=128,verbose_name='家庭地址',null=True)
    relation = models.CharField(max_length=128,verbose_name='关系',null=True)
    phone = models.CharField(max_length=128,verbose_name='电话号码',null=True)
    add_time = models.DateTimeField(auto_now_add=True,null=True)

    def __unicode__(self):
        return self.book_name