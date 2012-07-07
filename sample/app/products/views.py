# -*- coding: utf-8 -*-

from django import template
from django.shortcuts import render_to_response,redirect
from django.core.paginator import Paginator

import os

from models import Product,Category

PRODUCTS_IN_PAGE=4

def product_pager(category="all",items_in_page = PRODUCTS_IN_PAGE):
    if category == "all":
        return Paginator( 
                Product.objects.all() 
                , items_in_page) 
    else:
        return Paginator( 
                Product.objects.filter(category__slug=category)
                , items_in_page) 
    

def render(request,path):
    page = os.path.basename( path )
    return render_to_response( '%s.html' % page,
                        {} ,
                    context_instance=template.RequestContext(request),)

def product_item(request,id):
    return render_to_response( 'products/item.html' ,
                        {'product': Product.objects.get(id=id),} ,
                    context_instance=template.RequestContext(request),)
def product_category(request):
    return render_to_response( 'products/category.html' ,
                        {'categories': Category.objects.all().order_by('name'),} ,
                    context_instance=template.RequestContext(request),)

def product_page(request,category,page):
    pager = product_pager(category)
    p = pager.page(page)

    return render_to_response( 'products/page.html' ,
                    {'page':p, 
                     'category': category,
                    },
                    context_instance=template.RequestContext(request),)
