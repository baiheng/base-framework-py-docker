#!/bin/env python
# -*- coding:utf8 -*-

from sqlalchemy import Column, String, Integer, DateTime, text

from core.common.sqlalchemy_ctl import Base
from core.common.utility import create_table

from core.conf import settings


class User(Base):
    __tablename__ = 'account_user'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, server_default='')
    password = Column(String(50), nullable=False, server_default='')
    phone = Column(String(50), nullable=False, server_default='')
    create_time = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))


if settings.CREATE_TABLE:
    create_table("account_user")
