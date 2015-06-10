# -*- coding: utf-8 -*-

## get the logger used to log the mysite application
import logging

## the log
LOG = logging.getLogger('web2py.app.mysite')


## define the database connection
DB = DAL('sqlite://site.sqlite')


## define the category table
DB.define_table('CATEGORY',
                Field('TITLE', type = 'string', length = 128))

## define the message table
DB.define_table('MESSAGE',
                Field('TITLE', type = 'string', length = 512),
                Field('CONTENT', type = 'string', length = 1024 * 1024),
                Field('CATEGORY', type = 'reference CATEGORY'),
                Field('TIMESTAMP', type = 'datetime'))

## define the link group table
DB.define_table('LINK_GROUP',
                Field('NAME', type = 'string', length = 512))

## define the link table
DB.define_table('LINKS',
                Field('TIMESTAMP', type = 'datetime'),
                Field('ADDRESS', type = 'string', length = 512),
                Field('TITLE', type = 'string', length = 512),
                Field('DESCRIPTION', type = 'string', length = 1024 * 1024),
                Field('LINK_GROUP', type = 'reference LINK_GROUP'))
"""
## initialize the base information table like category and link group
DB.CATEGORY.insert(TITLE = 'C/C++')
DB.CATEGORY.insert(TITLE = 'Python')
DB.CATEGORY.insert(TITLE = 'Html CSS Javascript')
DB.CATEGORY.insert(TITLE = '生活')

DB.LINK_GROUP.insert(NAME = '编程开发')
DB.LINK_GROUP.insert(NAME = '设计艺术')
DB.LINK_GROUP.insert(NAME = '品味生活')
DB.LINK_GROUP.insert(NAME = '其他')
"""

## initialize the link category
LINK_CATEGORY = {}
for row in DB().select(DB.LINK_GROUP.ALL):
    LINK_CATEGORY[row.id] = row.NAME

## initialize the message category
MESSAGE_CATEGORY = {}
for row in DB().select(DB.CATEGORY.ALL):
    MESSAGE_CATEGORY[row.id] = row.TITLE
