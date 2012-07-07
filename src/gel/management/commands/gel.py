# -*- coding: utf-8 -*-

'''

.. todo::
    Find project root directroy

'''
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from optparse import make_option

import os 
import shutil

DEFAULT_DIR = "../www"

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (

        make_option('--dir',
            action='store',
            dest='dir',
            default=DEFAULT_DIR,
            help=u'Target Directory'),

    )

    def save_content(self,urlpath ):
        from django.test import client
        _c = client.Client()
        r = _c.get(urlpath)

        save_dir = DEFAULT_DIR + os.path.dirname(urlpath) 
        if not os.path.isdir(save_dir):
            os.makedirs(save_dir)

        open(DEFAULT_DIR + urlpath, 'w').write(r.content)

    def handle_default(self, *args, **options):
        ''' Run under project root
        '''

        #: ROOT
        if not os.path.isdir(options['dir']):
            os.makedirs(options['dir'] ) 

        #: STATIC
        self.STATIC = os.path.join(options['dir'] ,"static"  )
        if os.path.isdir(self.STATIC):
            shutil.rmtree(self.STATIC) 
        shutil.copytree('static',self.STATIC )       #: TODO "static" should be given as option

        #: MEDIA 
        #: MEDIA_ROOT shoul be relative to project root ( as of now )
        if settings.MEDIA_ROOT != "":
            print settings.MEDIA_ROOT
            self.MEDIA = os.path.join(options['dir'] , settings.MEDIA_ROOT )
            if os.path.isdir(self.MEDIA):
                shutil.rmtree(self.MEDIA) 
            shutil.copytree(settings.MEDIA_ROOT,self.MEDIA)  

        #: URLS
        m = __import__(settings.GEL_MODULE,globals(),locals(), 
                        settings.GEL_MODULE.split('.')[-1:] ) 
        
        for u in m.urls():
            self.save_content( u )

    def handle(self, *args, **options):
        command = args[0] if len(args) >0 else 'default'
        getattr(self, 'handle_%s'% command ,Command.handle_default)(self,*args,**options)
