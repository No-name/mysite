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

    # get all category from the database
    category = [row.TITLE for row in DB().select(DB.CATEGORY.TITLE)]

    # collect the message in our database



    # set which message page this function return
    response.whichPage = 'message'

    return dict(category = category)


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


    for row in DB().select(DB.LINKS.ALL):
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

def storeLink(request):

    post_vars = request.post_vars

    values = {}

    values['ADDRESS'] = post_vars['link']
    values['TITLE'] = post_vars['title']
    values['DESCRIPTION'] = post_vars['desc']
    values['LINK_GROUP'] = post_vars['category']

    for k in values:
        LOG.debug('store key ' + k + " : " + values[k])


    return True

    DB.LINKS.insert(**values)

    return True

def storeMessage(request):

    return True

def submit():
    """
    used to submit message and link data,
    this is an ajax response

    :return:
    """

    submitType = request.vars['type']

    LOG.info("submit type is " + submitType)

    if (submitType == 'link'):
        storeLink(request)
    elif (submitType == 'message'):
        storeMessage(request)

    return dict()
