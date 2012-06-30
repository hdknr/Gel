# -*- coding: utf-8 -*-

'''

.. todo::
    Find project root directroy

'''
from django.core.management.base import BaseCommand, CommandError
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
        #: ROOT
        if not os.path.isdir(options['dir']):
            os.makedirs(options['dir'] ) 

        #: STATIC
        self.STATIC = options['dir'] +"/static" 
        if os.path.isdir(self.STATIC):
            shutil.rmtree(self.STATIC) 
        shutil.copytree('static',self.STATIC )       #: TODO "static" should be given as option

        #: URLS
        self.save_content('/a/a/a/index.html')

#        print r.content
#        print dir(r)

    def handle(self, *args, **options):
        command = args[0] if len(args) >0 else 'default'
        getattr(self, 'handle_%s'% command ,Command.handle_default)(self,*args,**options)
