#!/bin/env python
# -*- coding:utf8 -*-

from core.common.mylog import logger
from core.common.base_view import BaseView
from core.celery_app.t_tasks import do_something


class UserView(BaseView):
    def get(self):
        logger.error("测试")
        do_something.delay()
        return self._response()

    def get_action_k(self):
        logger.info("testste")
        logger.info("测试")
        do_something.delay()
        return self._response()
