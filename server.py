#!/bin/env python
# -*-coding:utf-8-*-

import os
import importlib

# 先加载这里的logger
from core.common.mylog import logger
from core.conf import settings

from sanic import Sanic


app = Sanic(__name__)


modules = [
    'account',
]

def dispatch(item):
    async def _dispatch(*args, **kwargs):
        obj = item[1]
        kwargs["controller_obj"] = item[2]
        # 当item == 4 说明get post put delete 用默认function
        if len(item) in (3, 4):
            return obj(*args, **kwargs).dispatch()
        else:
            return obj(*args, **kwargs).dispatch(item[3])
    return _dispatch

methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]
for i in modules:
    urls_modules = importlib.import_module('core.{0}.urls'.format(i))
    for j in getattr(urls_modules, 'urls', []):
        url_prefix = "/v1/api/{0}/{1}".format(i, j[0])
        app.add_route(dispatch(j), url_prefix, methods=methods)
    for j in getattr(urls_modules, 'restful_urls', []):
        app.add_route(dispatch(j), j[0], methods=j[-1])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18289, debug=settings.DEBUG)
