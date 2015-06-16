# -*- coding: utf-8 -*-

import datetime

from lmtype import NoEscape

def link():
    """
    used to submit link data

    :return:
    """

    result = {}

    post_vars = request.post_vars

    values = {}

    values['ADDRESS'] = post_vars['link']
    values['TITLE'] = post_vars['title']
    values['DESCRIPTION'] = post_vars['desc']
    values['LINK_GROUP'] = post_vars['category']
    values['TIMESTAMP'] = datetime.datetime.now()

    DB.LINKS.insert(**values)

    result = {
        'type' : 'link',
        'link' : values['ADDRESS'],
        'title' : values['TITLE'],
        'desc' : values['DESCRIPTION']
    }

    return dict(result = result)

def message():
    """
    used to submit message data

    :return:
    """

    result = {}

    post_vars = request.post_vars

    values = {}

    values['TITLE'] = post_vars['title']
    values['CONTENT'] = post_vars['message']
    values['CATEGORY'] = post_vars['category']
    values['TIMESTAMP'] = datetime.datetime.now()

    LOG.debug("Content : " + values['CONTENT'])

    DB.MESSAGE.insert(**values)

    result = {
        'title' : values['TITLE'],
        'category' : MESSAGE_CATEGORY[int(values['CATEGORY'])],
        'date' : values['TIMESTAMP'].date(),
        'content' : values['CONTENT']
    }

    return dict(result = result)
