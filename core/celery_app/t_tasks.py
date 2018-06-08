#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import time

from core.conf import settings
from core.common.mylog import logger
from core.celery_app import celery


@celery.task
def do_something():
    logger.info("start_work")
    time.sleep(10)
    logger.info("end_work")
