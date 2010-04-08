#!/usr/bin/env python
# encoding: utf-8
"""
MotiniController.py

Created by mikepk on 2009-12-08.
Copyright (c) 2009 Michael Kowalchik. All rights reserved.
"""

import sys
import os
import unittest

from webob.dec import wsgify
from webob import Response, Request

import re
from paste.proxy import Proxy, TransparentProxy
from lxml import html

from deliverance.middleware import FileRuleGetter,DeliveranceMiddleware
from deliverance.ruleset import RuleSet

from deliverance.proxy import ProxySet
from deliverance.proxy import ProxySettings

from lxml.etree import XML
import urlparse

import pickle


class MotiniController():
    '''MotiniController'''

    def __init__(self):
        self.host = ""
        self.my_path_info = ""
        
    def _proxy_middleware(self, req, caching=True):
        if not req.path_info:
            req.path_info = '/'
        # if self.my_path_info != '/':
        #     # self.my_path_info = '/'+self.my_path_info
        #     #proxy_url = '''http://%s%s''' % (str(self.host),str(req.path_info))
        # else:
        #     proxy_url = '''http://%s/''' % (str(self.host))
        proxy_url = '''http://%s/''' % (str(self.host))

        # the proxied host, used for link re-writing
        dest_href = '''http://%s/''' % (str(self.host))    

        # stop caching and gzip encoding
        # req.remove_conditional_headers(remove_encoding=True)

        # suppress these headers in proxy requests
        stop_headers = ['if-none-match','if-modified-since']
        px = Proxy(proxy_url,suppress_http_headers=stop_headers)
        lw = LinkRewriterMiddleware(px,dest_href,self.base_script)
        return lw


    @wsgify
    def clip(self,req):
        '''proxy load a page for clipping'''
        self.base_script = '/motini/clip/'

        req.path_info_pop()
        req.path_info_pop()
        self.host = req.path_info_pop()
        self.my_path_info = req.path_info

        # add the proxy and link-rewriter WSGI middleware to these request on
        # the fly
        proxy = self._proxy_middleware(req)
        return req.get_response(proxy)


    @wsgify
    def theme(self,req):
        '''Proxy load a page for applying a theme.'''
        self.base_script = '/motini/theme/'

        req.path_info_pop()
        req.path_info_pop()
        self.host = req.path_info_pop()
        self.my_path_info = req.path_info

        try:
            rule_file = open('/var/tmp/rules_list.dat','r')
            temporary_rules = pickle.load(rule_file)
        except pickle.PickleError:
            temporary_rules = None
        
        # add the proxy, link-rewriter, and deliverance x-from layers to the WSGI middleware 
        # on this request
        motini_rules = MotiniRules(temporary_rules)

        proxy = self._proxy_middleware(req)
        deliv_mw = DeliveranceMiddleware(proxy, motini_rules)
        resp = req.get_response(deliv_mw)
        
        return resp

import urlparse

class LinkRewriterMiddleware(object):
    """Rewrites the response, assuming the HTML was generated as though based at
    `dest_href`, and needs to be rewritten for the incoming request"""

    # The normal __init__, __call__ pattern:
    def __init__(self, app, dest_href, base):
        self.app = app
        if dest_href.endswith('/'):
            dest_href = dest_href[:-1]
        self.dest_href = dest_href
        self.base_script = base

    @wsgify
    def __call__(self, req):

        dest_path = req.path_info
        dest_href = self.dest_href + dest_path
        # req.application_url is the base URL not including path_info or the query string:
        req_href = req.application_url
        def link_repl_func(link):
            #remove all relative links
            # link = urlparse.urljoin(dest_href, link)
            # return link

            # Rewrite all links from the proxied domain to map
            # to the proxy itself
            if not link.startswith(dest_href):
                # Not a local link
                return link
            new_url = req_href + '/' + link[len(dest_href):]
            return new_url
        resp = req.get_response(self.app)
        # This decodes any possible gzipped content:
        resp.decode_content()
        if (resp.status_int == 200
            and resp.content_type == 'text/html'):
            doc = html.fromstring(resp.body, base_url=dest_href)
            doc.rewrite_links(link_repl_func)
            resp.body = html.tostring(doc)
        # Redirects need their redirect locations rewritten:
        if resp.location:
            # self.dest_href = resp.location
            link = urlparse.urljoin(dest_href, resp.location)
            match = re.search(r'^([^\/]*)(.*)',resp.location.lstrip('http://'))
            if match:
                new_host = match.group(1)
                new_path_info = match.group(2)
                self.host = new_host
                self.my_path_info = new_path_info
            resp.location = '%s%s%s' % (self.base_script,self.host,self.my_path_info)
            # resp.location = req_href + resp.location
            # resp.location = link_repl_func(resp.location)
        return resp
        # return resp(environ, start_response)


class MotiniRules(object):
    '''A placeholder rules object that is callable to satisfy how Deliverance works.'''

    def __init__(self,rules=None):
        '''init the Motini rules.'''

        
        rules_xml = '''<?xml version="1.0"?>
        <ruleset>
        <match path="/motini/theme" class="swap"/>
        <rule class="swap" suppress-standard="1">
        <!--  <theme href="/theme/iphone.html"/>-->
        	<theme href="/theme/index.html"/>
            '''
        if rules:
            for rule in rules:
                rules_xml += '''<%s content="%s" theme="%s" />'''% (rule.action,rule.content,rule.theme)
        rules_xml += '''
        </rule>
        </ruleset>'''

        url = 'http://motini.net/'
        try:
            doc = XML(rules_xml, base_url=url)
        except XMLSyntaxError, e:
            raise Exception('Invalid syntax in %s: %s' % (url, e))
        assert doc.tag == 'ruleset', (
            'Bad rule tag <%s> in document %s' % (doc.tag, url))

        self.rules_set = RuleSet.parse_xml(doc, url)

    def __call__(self, get_resource, app, orig_req):
        '''Always return this rules set after parsing.'''
        return self.rules_set




class MotiniControllerTests(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()