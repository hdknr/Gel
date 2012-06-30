# -*- coding: utf-8 -*-

from datetime import datetime

def site(request):
    return { 
                "META": META,
           }   

META = {
        'SITE_NAME': 'Vegene',
        'CORP_NAME': 'Vegene',
        'CORP_INTRODUCTION': 'Fresh Vegetable for You',
    }
