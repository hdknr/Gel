# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from  django.core.urlresolvers import reverse

class Content(models.Model):
    slug  = models.CharField(u'Content Slug',max_length=200,db_index=True,unique=True) 
    title = models.CharField(u'Content Title',max_length=200,db_index=True,blank=True,null=True)
    text  = models.TextField(u'Content Text',)
    media = models.TextField(u'Content Media',default=None,null=True,blank=True)
    dt_publish = models.DateTimeField(u'Content Publish Date Time',default=datetime.now )

    class Meta:
        abstract=True

class News(Content):
    def get_absolute_url(self):
        return reverse("contents_news_item",kwargs={'id':self.id} )

def context(request):
    return {
                "LATEST_NEWS" : News.objects.all()[:5],   
           } 

