# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273537674.435544
_template_filename='/Users/nateaune/code/motini-github/motini/templates/rules.mako'
_template_uri='/rules.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rules = context.get('rules', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0"?>\n    <ruleset>\n    <match path="/motini/theme" class="swap"/>\n    <rule class="swap" suppress-standard="1">\n    \t<theme href="/theme/index.html"/>\n')
        # SOURCE LINE 6
        if rules:
            # SOURCE LINE 7
            for rule in rules:
                # SOURCE LINE 8
                __M_writer(u'    <')
                __M_writer(unicode(rule.action))
                __M_writer(u' content="')
                __M_writer(unicode(rule.content))
                __M_writer(u'" theme="')
                __M_writer(unicode(rule.theme))
                __M_writer(u'" />\n')
                pass
            pass
        # SOURCE LINE 11
        __M_writer(u'</rule>\n</ruleset>')
        return ''
    finally:
        context.caller_stack._pop_frame()


