#!/usr/bin/env python
# encoding: utf-8
"""
IndexController.py

Created by mikepk on 2009-12-07.
Copyright (c) 2009 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

from webob.dec import wsgify
from webob import Response

from Rule import Rule

from BaseController import BaseController

import pickle
# from app.models.Rule import Rule

class StartController(BaseController):
    '''Pybald controller IndexController'''
    @wsgify
    def index(self,req):
        data = {}
        try:
            form_vars = req.params
            data['url'] = form_vars["u"]
            if data['url'].startswith('http://'): data['url'] = data['url'][7:]
        except KeyError:
            data['url'] = ''
            
        return self.show_template('start.mako',data)


    @wsgify
    def write_rules(self,req):
        '''Get the posted rules and write them to the temporary session table.'''
        # read post values and save them. Intended as an Ajax call.

        form_vars = req.POST
            #print "Failed to open the rules file."
            # rule_file = open('/var/tmp/rules_list.dat','wb')

        rules = []
        try:
            try:
                rule_file = open('/var/tmp/rules_list.dat','rb')
            except:
                pass
            rules = pickle.load(rule_file)
            rule_file.close()
        except:
            rules = []
            #return "Failed to read the rules."

        try:
            command = form_vars['command']
            if command == 'clear':
                try:
                    rule_file = open('/var/tmp/rules_list.dat','wb')
                    rules = []
                    pickle.dump(rules,rule_file)
                    rule_file.close()
                except:
                    pass
                # self.session.cachestore['temp_rules'] = rules
                # self.session.save()
                return 'success'
        except KeyError:
            pass



        try:
            r = Rule()
            r.action = form_vars['action']
            r.content = form_vars['content']
            r.theme = form_vars['theme']
        except KeyError:
            return "failed"


        rules.append(r)
        try:
            rule_file = open('/var/tmp/rules_list.dat','wb')
            pickle.dump(rules,rule_file)
        except:
            return "Failed to Write rules"

        # self.session.cachestore['temp_rules'] = rules
        # self.session.save()
        return 'success'

class StartControllerTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()