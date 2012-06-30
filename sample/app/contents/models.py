# -*- coding: utf-8 -*-
from django.db import models


class Content(models.Model):
    slug  = models.CharField(u'Content Slug',max_length=200,db_index=True,unique=True) 
    title = models.CharField(u'Content Title',max_length=200,db_index=True,blank=True,null=True)
    text  = models.TextField(u'Content Text',)
    media = models.TextField(u'Content Media',default=None,null=True,blank=True)

class Page(models.Model):
    contents = models.ManyToManyField(Content,default=None,null=True,blank=True )
    title = models.CharField(u'Page Title',max_length=200,db_index=True,blank=True,null=True)
    
