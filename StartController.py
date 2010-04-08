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

import pickle
# from app.models.Rule import Rule

class StartController():
    '''Pybald controller IndexController'''
    @wsgify
    def index(self,req):
        try:
            form_vars = req.params
            self.url = form_vars["u"]
            self.url = self.url.lstrip('http://')
        except KeyError:
            self.url = ''
    
        start_page = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
        <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

                <title>Motini</title>

          <script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>
          <script type="text/javascript" src="/js/jquery-ui-1.7.1.custom.min.js"></script>
          <script type="text/javascript" src="/js/jquery.layout.min.js"></script>
        <!--  <script type="text/javascript" src="js/dom.js"></script> -->
          <script type="text/javascript" src="/js/banjo.js"></script>
          <link rel="stylesheet" href="/css/banjo.css" type="text/css" media="screen" title="no title" charset="utf-8">
          <link rel="stylesheet" href="/css/smoothness/jquery-ui-1.7.1.custom.css" type="text/css" media="screen" title="no title" charset="utf-8">

        </head>

        <body>

          <div id="info">
            <div id="status_box">
              <img src='/images/motini-logo-200.jpg' alt="Motini" id="logo" />
            </div>
            <!-- <div id="rules_box"> -->
        <div id="controls_box">
              <h1>Mix your own Motini!</h1>
              <form id="url_form" method="GET" action="" >
                <label>URL:</label> <input type="text" id="u" name="u" value="%s" />
                <input type="submit" value="Mix" />
              </form>
        </div>

        <div id="actions_box">
              <h1><a href="/rules.xml">Show the current rules</a></h1>
              <div id="rules"></div>
            <!-- </div> -->
            <!-- <div id="actions_box">
              <div id="actions"> -->
                <a id="clear_rules" href="#">Dump out this Motinin and start over.</a><br/>
              <!-- </div> -->
              <img id="loading" src="/images/ajax-loader.gif"/>
              <!-- <div id="url"> -->
                <h4>To save your Motini you have to <strong>create an account</strong>.</h4>
              <!-- </div>
            </div> -->
            <!-- <div id="motini_url"> -->

        </div>
          </div>''' % (self.url)
        if self.url:
            start_page += '''<iframe id="delivsource" name="delivsource" src="/motini/clip/%s"></iframe>
            <iframe id="delivtarget" name="delivtarget" src="/motini/theme/%s"></iframe>''' % (self.url, self.url)
        else:
            start_page += '''<div id="delivsource">
            <h2>Type in a URL to mix into a Motini!</h2>
        </div>'''

        start_page += '''</body>
        </html>'''

        return start_page

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
            return "Failed to read the rules."

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