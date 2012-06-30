# -*- coding: utf-8 -*-

from datetime import datetime
from django.conf import settings

def relative_root(request):
    if not getattr(settings,'STATIC_RELATIVE',False):
        return ""
    n = request.path.count('/') 
    return "." + '/..' * (n-1)

def params(request):
    return { 
                "RELATIVE_ROOT": relative_root(request),
           }   
