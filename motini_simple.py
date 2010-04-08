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

def main():
    '''A simple server startup if module is called directly'''
    from paste.evalexception import EvalException

    # a stupid static file server to serve data in 'content'
    from static_serve import static_serve
    from paste.httpserver import serve

    # Dispatcher is a rock-dumb URL path comarison to call the three motini functions
    run_pipeline = Dispatcher(static_serve(path="content"))
    serve(EvalException(run_pipeline), '0.0.0.0', 8000, socket_timeout=2)

if __name__ == '__main__':
    main()
