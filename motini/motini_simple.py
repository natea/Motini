#!/usr/bin/env python
# encoding: utf-8
"""
motini_simple.py

Created by mikepk on 2010-04-08.
Copyright (c) 2010 Michael Kowalchik. All rights reserved.
"""

import sys
import getopt

from Dispatcher import Dispatcher

help_message = '''
Sample Motini web-framework-less
'''

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

import urlparse

def app_factory(global_conf=None, **app_conf):
    # a stupid static file server to serve data in 'content'
    from static_serve import static_serve

    # Dispatcher is a rock-dumb URL path comarison to call the three motini functions
    app = static_serve(path="content")
    app = Dispatcher(app)
    return app

def main():
    '''A simple server startup if module is called directly'''
    from paste.evalexception import EvalException
    from paste.httpserver import serve


    app = app_factory()
    app = EvalException(app)
    
    serve(app, '0.0.0.0', 8000, socket_timeout=2)

if __name__ == '__main__':
    main()
