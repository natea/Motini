#!/usr/bin/env python
# encoding: utf-8
"""
RulesController.py

Created by mikepk on 2010-04-08.
Copyright (c) 2010 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

from webob.dec import wsgify
from webob import Response
import pickle
from BaseController import BaseController

class RulesController(BaseController):
    '''Pybald controller RulesController'''

    @wsgify
    def index(self,req):
        data = {}
        try:
            rule_file = open('/var/tmp/rules_list.dat','r')
            data['rules'] = pickle.load(rule_file)
        except:
            data['rules'] = None            
        
        rules_xml = self.show_template('rules.mako',data)
        resp = Response()
        resp.headerlist = [('Content-type', 'text/xml; charset=UTF-8')]
        resp.body = rules_xml
        return resp

class RulesControllerTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()