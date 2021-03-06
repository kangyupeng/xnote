# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2017
# @modified 2018/07/28 12:16:59

def element(tag, text, clazz):
    """
        >>> element('span', '123', 'test')
        "<span class='test'>123</span>"
    """
    return "<%s class='%s'>%s</%s>" % (tag, clazz, text, tag)

def span(text, clazz = 'xnote-span'):
    return element("span", text, clazz)


def pre(text, clazz = 'xnote-pre'):
    """
        >>> pre('hello')
        "<pre class='xnote-pre'>hello</pre>"
    """
    return element("pre", text, clazz)

def div(text, clazz = 'xnote-div'):
    return element("div", text, clazz)

def link(name, link = None, clazz = "xnote-link"):
    if link is None:
        link = name
    return "<a class='%s' href='%s'>%s</a>" % (clazz, link, name)

