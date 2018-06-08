#!/bin/env python
# -*-coding:utf-8-*-

from core.account.views.user_view import UserView

from core.account.controllers import user_obj


urls = [
    ("user", UserView, user_obj),
]


restful_urls = [
    ("/v1/account/a", UserView, user_obj, "get", ["GET"]),
]
