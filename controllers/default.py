# -*- coding: utf-8 -*-


def index():
    """
    get the main page

    :return:
    """

    return dict()


def message():
    """
    get the message page

    :return:
    """

    response.whichPage = 'message'

    return dict()


def links():
    """
    get the links page

    :return:
    """

    response.whichPage = 'links'

    return dict()


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
