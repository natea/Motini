#!/usr/bin/env python
# encoding: utf-8
"""
Rule.py

Created by mikepk on 2009-12-09.
Copyright (c) 2009 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

class Rule():
    '''A Rule object for associating rules with users and sites.'''

    def __init__(self,action='replace',content=None,theme=None):
        self.rule_id = None
        self.user_id = None
        self.site_url = None
        self.action = action
        self.content = content
        self.theme = theme

class RuleTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()