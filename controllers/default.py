# -*- coding: utf-8 -*-

from lmtype import NoEscape

def index():
    """
    get the main page

    :return:
    """

    return dict()


def messages():
    """
    get the message page

    :return:
    """

    # get all category from the database
    category = {}
    for row in DB().select(DB.CATEGORY.ALL):
        category[row.id] = row.TITLE

    # collect the message in our database
    messages = []
    for row in DB().select(DB.MESSAGE.ALL, orderby = ~DB.MESSAGE.TIMESTAMP):
        message = {
            'title' : row.TITLE,
            'content' : row.CONTENT,
            'category' : MESSAGE_CATEGORY[row.CATEGORY],
            'date' : row.TIMESTAMP.date()
        }

        messages.append(message)

    # set which message page this function return
    response.whichPage = 'messages'

    return dict(category = category, messages = messages)


def links():
    """
    get the links page

    :return:
    """

    links = {}
    groups = {}
    # get all the link groups from the database
    for row in DB().select(DB.LINK_GROUP.ALL):
        groups[row.id] = row.NAME
        links[row.id] = []


    for row in DB().select(DB.LINKS.ALL, orderby = ~DB.LINKS.TIMESTAMP):
        link = {
            'title' : row.TITLE,
            'desc' : row.DESCRIPTION,
            'link' : row.ADDRESS
        }

        links[row.LINK_GROUP].append(link)


    response.whichPage = 'links'

    return dict(groups = groups, links = links)


def article():
    """
    get the article page

    :return:
    """

    response.whichPage = 'article'

    return dict()


def about():
    """
    about information page

    :return:
    """

    response.whichPage = 'about'

    return dict()
