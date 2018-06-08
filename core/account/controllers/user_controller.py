#!/bin/env python
# -*-coding:utf-8-*-

from core.common.base_controller import BaseController

from core.account.models import User


class UserController(BaseController):
    pass


user_obj = UserController(User)
