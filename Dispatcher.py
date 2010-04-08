#!/usr/bin/env python
# encoding: utf-8
"""
Dispatcher.py

Created by mikepk on 2010-04-08.
Copyright (c) 2010 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

from routes import redirect_to

from webob.dec import wsgify
from webob import exc, Request, Response

from StartController import StartController
from MotiniController import MotiniController

class Dispatcher():
    '''Dispatcher'''
    def __init__(self,app=None):
        self.start = StartController()
        self.motini = MotiniController()
        self.app = app

        
    #@wsgify
    def __call__(self,environ,start_response):
        req = Request(environ)
        if req.path_info.startswith('/start'):
            if req.method == "POST":
                return self.start.write_rules(environ,start_response)
            return self.start.index(environ,start_response)
        elif req.path_info.startswith('/motini/clip'):
            print req.path_info
            print req.application_url
            return self.motini.clip(environ,start_response)
        elif req.path_info.startswith('/motini/theme'):
            return self.motini.theme(environ,start_response)

        #resp(environ, start_response)
        if self.app:
            return self.app(environ,start_response)
        return exc.HTTPNotFound()(environ,start_response)


class DispatcherTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()