#!/usr/bin/env python
# encoding: utf-8
"""
TemplateEngine.py

Created by mikepk on 2010-05-09.
Copyright (c) 2010 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

from mako.lookup import TemplateLookup

class TemplateEngine:
    def __init__(self):
        '''Init the Template system'''
        self.path = os.path.dirname( os.path.realpath( __file__ ) )
        self.lookup = TemplateLookup(directories=[os.path.join(self.path,'templates')], module_directory=os.path.join(self.path,'templates','template_cache'), input_encoding='utf-8',output_encoding='utf-8')

    def __call__(self,template_name,context_data=None):
        '''Callable method that executes the template.'''
        mytemplate = self.lookup.get_template("/"+template_name)
        return mytemplate.render(**context_data)

engine = TemplateEngine()

class TemplateEngineTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()