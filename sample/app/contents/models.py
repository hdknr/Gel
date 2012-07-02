# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

from  django.core.urlresolvers import reverse

class Content(models.Model):

    def image_path_main(self,filename):
        return "image/main/"+ filename

    def image_path_mobile(self,filename):
        return "image/mobile/"+ filename

    def image_path_thumb(self,filename):
        return "image/thumb/"+ filename

    slug  = models.CharField(u'Content Slug',max_length=200,db_index=True,unique=True) 
    title = models.CharField(u'Content Title',max_length=200,db_index=True,blank=True,null=True)
    text  = models.TextField(u'Content Text',)
    media = models.TextField(u'Content Media',default=None,null=True,blank=True)
    image_main  = models.ImageField(u'Content Main Image',default=None,null=True,blank=True,upload_to=image_path_main)
    image_mobile = models.ImageField(u'Content Mobile Image',default=None,null=True,blank=True ,upload_to=image_path_mobile)
    image_thumb = models.ImageField(u'Content Thumbnail Image',default=None,null=True,blank=True,upload_to=image_path_thumb )
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

