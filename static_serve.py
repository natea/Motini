#!/usr/bin/env python
# encoding: utf-8
"""
static_serve.py

Created by mikepk on 2009-11-17.
Copyright (c) 2009 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

#import project
import mimetypes
from webob import Response, exc

class static_serve:
    def __init__(self, application=None, path="/"):
        """ path is directory where static files are stored
        """
        project_path = os.path.dirname( os.path.realpath( __file__ ) )
        
        self.path = os.path.join(project_path,path)
        self.application = application


    def send_file(self, file_path, size):
        '''Send an iterable file.'''
        BLOCK_SIZE = 64 * 1024
        f = open(file_path)# as f:
        block = f.read(BLOCK_SIZE)
        while block:
            yield block
            block = f.read(BLOCK_SIZE)
        f.close()


    def __call__(self,environ,start_response):
        '''A simple static file server.'''
        file_path = os.path.join(self.path,environ['PATH_INFO'].lstrip('/') )
        if not os.path.isfile(file_path):
            if self.application:
                return self.application(environ, start_response)
            else:
                return exc.HTTPNotFound()(environ,start_response)
                
        mimetype, encoding = mimetypes.guess_type(file_path)

        size = os.path.getsize(file_path)
        headers = [
            ("Content-type", mimetype),
            ("Content-length", str(size)),
        ]
        start_response("200 OK", headers)
        return self.send_file(file_path, size)

class static_serveTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()