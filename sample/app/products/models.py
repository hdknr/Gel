# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    slug = models.CharField(u'Category Slug',max_length=200,unique=True,db_index=True )
    name = models.CharField(u'Category Name',max_length=20, )
    description = models.TextField(u'Category Detail')

    def __unicode__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,verbose_name=u'Product Category' )
    code = models.CharField(u'Product Code',max_length=15,db_index=True,unique=True,)
    name = models.CharField(u'Product Name',max_length=20,) 
    slug = models.CharField(u'Product Slug',max_length=200,db_index=True,unique=True) 
    price =  models.DecimalField(u'Price',default=0, max_digits=11, decimal_places=0)
    description = models.TextField(u'Product Detail')

    def __unicode__(self):
        return self.name
