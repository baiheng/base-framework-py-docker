#!/bin/env python
# -*- coding:utf8 -*-

from .settings_production import BaseConfig


class LocalConfig(BaseConfig):
    DEBUG = True
    ECHO_SQL = False
    CREATE_TABLE = True

    # token
    # 7天有效期
    TOKEN_TIMEOUT = 7 * 24 * 60 * 60 
    PRIVATE_KEY = '8434567812345678'

    # 数据查询ip
    MYSQL_HOST = '**'
    MYSQL_PORT = 3306
    MYSQL_USER = "**"
    MYSQL_PWD = "**"
    MYSQL_DB = "test"
