# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273542405.56722
_template_filename='/Users/nateaune/code/motini-github/motini/templates/start.mako'
_template_uri='/start.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\n    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n    <head>\n            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n            <title>Motini</title>\n\n      <script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>\n      <script type="text/javascript" src="/js/jquery-ui-1.7.1.custom.min.js"></script>\n      <script type="text/javascript" src="/js/jquery.layout.min.js"></script>\n      <script type="text/javascript" src="/js/banjo.js"></script>\n      <link rel="stylesheet" href="/css/banjo.css" type="text/css" media="screen" title="no title" charset="utf-8">\n      <link rel="stylesheet" href="/css/smoothness/jquery-ui-1.7.1.custom.css" type="text/css" media="screen" title="no title" charset="utf-8">\n\n    </head>\n\n    <body>\n\n      <div id="info">\n          \n        <div id="status_box">\n          MOTINI\n        </div>\n        \n        <div id="controls_box">\n              <h1>Type in the URL of a site you want to theme</h1>\n              <form id="url_form" method="GET" action="" >\n                <label>URL:</label> <input type="text" id="u" name="u" value="')
        # SOURCE LINE 29
        __M_writer(unicode(url))
        __M_writer(u'" />\n                <input type="submit" value="Theme it!" />\n              </form>\n        </div>\n\n        <div id="actions_box">\n              <a href="/rules.xml">Show current rules</a><br/>\n              <a id="clear_rules" href="#">Clear rules</a><br/>\n              <img id="loading" src="/images/ajax-loader.gif"/>\n\n        </div>\n      </div>\n      \n')
        # SOURCE LINE 42
        if url:
            # SOURCE LINE 43
            __M_writer(u'        <iframe id="delivsource" name="delivsource" src="/motini/clip/')
            __M_writer(unicode(url))
            __M_writer(u'"></iframe>\n        <iframe id="delivtarget" name="delivtarget" src="/motini/theme/')
            # SOURCE LINE 44
            __M_writer(unicode(url))
            __M_writer(u'"></iframe>\n')
            # SOURCE LINE 45
        else:
            # SOURCE LINE 46
            __M_writer(u'        <div id="delivsource">\n            <div style="width:500px; margin:50px;">\n<h1>\n    What is Motini?\n</h1>\n<p>\n    Motini is a tool to easily theme a website using a point-n-click interface. By identifying elements from your content source and identifying where in your theme you want those elements to go, you can create rules that will move the dynamic content from your CMS or dynamic web application.\n</p>\n<h2>\n    How does it work\n</h2>\n<p>\n    Motini works by leveraging <a href="http://deliveranceproject.org">Deliverance</a>, a middleware proxy which reads a rules file that tells Deliverance which elements in your content source should be mapped to which placeholder elements in your static theme. It uses common CSS selectors to identify these elements, but it also works with XPath expressions.\n</p>\n<p>\n    Motini provides a point-n-click to select these elements and write out the resulting rules file as XML. This rules file can then be used in a production environment with the Deliverance proxy using these rules to govern the HTML transformations. The Deliverance proxy sits in between Apache (or whatever HTTP server you use) and your CMS to transform the HTML before it\'s returned to the browser.\n</p>\n<h2>\n    Getting started\n</h2>\n<p>\n    Motini loads two panes in the browser: a source pane on the left and a destination pane on the right.\n</p>\n<p>\n    In the source pane, you supply a URL of a content source that you want to theme. For example, if you enter http://drupal.org, then it will load the Drupal site in the left source pane.\n</p>\n<p>\n    In the destination pane is the theme that you want to use for your site. Currently, there is only one theme available, but in the future we plan to make many themes available, and even provide the option to supply your own theme.\n</p>\n<h2>\n    How can I learn more?\n</h2>\n<p>Sign up to be on the announcement list to be notified when Motini is ready for public use. See the signup form on the right.</p>\n<p>\n    If you are a developer and want to get involved, you can check out the <a href="http://github.com/natea/Motini">code</a> on Github and join the <a href="http://groups.google.com/group/motini-dev/">Motini developers list.</a> <a name="#signup"></a>\n</p>\n</div>\n</div>\n        <div id="delivtarget">\n        <h2>Short video tutorial</h2>\n<object width="560" height="340"><param name="movie" value="http://www.youtube.com/v/MIYiDIK5z6c&hl=en_US&fs=1&rel=0&color1=0x006699&color2=0x54abd6"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/MIYiDIK5z6c&hl=en_US&fs=1&rel=0&color1=0x006699&color2=0x54abd6" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="560" height="340"></embed></object>\n\n        <h2>Signup for more info</h2>\n        <p>\n            <iframe src="http://spreadsheets.google.com/embeddedform?key=t-kqsAwyZhErhkOQ0jlXEHQ" width="400" height="691" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>\n        </p>\n        \n')
            pass
        # SOURCE LINE 94
        __M_writer(u'        </div>\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


