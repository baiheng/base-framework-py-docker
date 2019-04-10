#!/bin/env python
# -*- coding:utf8 -*-


class BaseConfig(object):
    DEBUG = False
    ECHO_SQL = False
    CREATE_TABLE = False

    # 3小时后自动重连mysql
    MYSQL_CONNECT_TIMEOUT = 3 * 24 * 60 * 60

    # token
    # 7天有效期
    TOKEN_TIMEOUT = 7 * 24 * 60 * 60 
    PRIVATE_KEY = '8434567812345878'

    # 数据查询ip
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = "**"
    MYSQL_PWD = "**"
    MYSQL_DB = "test"

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_PWD = ""

    CELERY_BROKER_DB = 5
    CELERY_BACKEND_DB = 7
    CELERY_BROKER_URL = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, CELERY_BROKER_DB)
    CELERY_RESULT_BACKEND = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, CELERY_BACKEND_DB)
