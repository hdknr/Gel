# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import *

### Category 
class CategoryAdmin(admin.ModelAdmin):
    list_display=('slug','name','description',)
admin.site.register(Category,CategoryAdmin)

### Product 
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','code','slug','price','description',)
admin.site.register(Product,ProductAdmin)
