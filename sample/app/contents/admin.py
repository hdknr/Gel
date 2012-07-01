# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import *

### News
class NewsAdmin(admin.ModelAdmin):
    list_display=('slug','dt_publish','title','media','text',)
admin.site.register(News,NewsAdmin)
