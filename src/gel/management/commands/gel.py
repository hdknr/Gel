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

    def handle_default(self, *args, **options):
        #: ROOT
        if not os.path.isdir(options['dir']):
            os.makedirs(options['dir'] ) 

        #: STATIC
        STATIC = options['dir'] +"/static" 
        if os.path.isdir(STATIC):
            shutil.rmtree(STATIC) 
        shutil.copytree('static',STATIC )       #: TODO "static" should be given as option

        #: URLS
        from django.test import client
        _c = client.Client()
        r = _c.get('/index.html') 
        open(DEFAULT_DIR + '/index.html', 'w').write(r.content)
#        print r.content
#        print dir(r)

    def handle(self, *args, **options):
        command = args[0] if len(args) >0 else 'default'
        getattr(self, 'handle_%s'% command ,Command.handle_default)(self,*args,**options)
