#!/usr/bin/env python
# encoding: utf-8
"""
BaseController.py

Created by mikepk on 2010-05-09.
Copyright (c) 2010 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest
from TemplateEngine import engine


class BaseController:
    def __init__(self):
        self.show_template = engine

class BaseControllerTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()