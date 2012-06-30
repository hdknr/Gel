# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import *

### Content
class ContentAdmin(admin.ModelAdmin):
    list_display=('slug','title','media','text',)
admin.site.register(Content,ContentAdmin)

### Page
class PageAdmin(admin.ModelAdmin):
    list_display=('title',)
admin.site.register(Page,PageAdmin)
