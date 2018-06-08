#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery
from celery.schedules import timedelta, crontab

from core.conf import settings

celery = Celery('celeryapps',
                broker=settings.CELERY_BROKER_URL,
                backend=settings.CELERY_RESULT_BACKEND,
                )
celery.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_IMPORTS=[
        'core.celery_app.t_tasks',
    ],
    #CELERY_ROUTES={
    #    "celery_app.t_tasks.check_vm_stopped": {"queue": "check_vm_stopped"},
    #    "celery_app.vm_tasks.check_vm_running": {"queue": "check_vm_running"},
    #},
    #CELERYBEAT_SCHEDULE={
    #    'every_hour': {
    #        'task': 'celery_app.zabbix_tasks.update_task',
    #        'schedule': timedelta(hours=1),
    #    },
    #    'every_week': {
    #        'task': 'celery_app.certificate_tasks.query_task',
    #        'schedule': crontab(minute=30, hour=0, day_of_week=1)
    #    }
    #},
)

# 启动worker：
# $ cd /path
# $ celery worker -A core.celery_app -l info
# 或者 $ celery worker -A core.celery_app:celery -l info
#
# 启动beat
# $ celery beat -A core.celery_app

# 调用celery任务示例:
# from core.celery_app import vm_tasks
# vm_tasks.vm_install.delay(**args)
