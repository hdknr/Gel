# -*- coding: utf-8 -*-

from django import template
from django.shortcuts import render_to_response,redirect
import os

def render(request,path):
    page = os.path.basename( path )
    return render_to_response( '%s.html' % page,
                        {} ,
                    context_instance=template.RequestContext(request),)

