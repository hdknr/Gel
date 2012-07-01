# -*- coding: utf-8 -*-

from django import template
from django.shortcuts import render_to_response,redirect
from django.core.paginator import Paginator

import os

from models import News

def render(request,path):
    page = os.path.basename( path )
    return render_to_response( '%s.html' % page,
                        {} ,
                    context_instance=template.RequestContext(request),)

def news_item(request,id):
    if id == 'index':
        return news_page(request,1 )
    return render_to_response( 'news/item.html' ,
                        {'news': News.objects.get(id=id),} ,
                    context_instance=template.RequestContext(request),)

def news_page(request,page):
    pager = Paginator( News.objects.all() , 4) 
#    p= pager.page( max(1,min(page ,pager.num_pages)) )
    p = pager.page(page)
#    print ">>>",page,  pager.num_pages, p.previous_page_number(),p.next_page_number()

    return render_to_response( 'news/page.html' ,
                    {'page':p, },
                    context_instance=template.RequestContext(request),)
