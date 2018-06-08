#!/bin/bash
#===============================================================================
#
#          FILE:  start.sh
# 
#         USAGE:  ./start.sh 
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
#       CREATED:  2018年06月06日 17时33分38秒 CST
#      REVISION:  ---
#===============================================================================

watchmedo auto-restart --patterns="*.py;*.ini" --recursive "./server.py"
