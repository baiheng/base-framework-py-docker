#!/bin/bash
#===============================================================================
#
#          FILE:  run-docker.sh
# 
#         USAGE:  ./run-docker.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  chenbaiheng (), chenbaiheng@xunlei.com
#       COMPANY:  XunLei Networking Tech
#       VERSION:  1.0
#       CREATED:  2018年06月06日 19时28分50秒 CST
#      REVISION:  ---
#===============================================================================

pip3 install -r /work/requirement.txt
ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
rm /tmp/* -rf
#python3.6 /work/server.py &

celery multi start worker -A core.celery_app -l info \
      --pidfile="/tmp/celery.pid" \
      --logfile="/work/log/celery.log"

tail -f /dev/null
