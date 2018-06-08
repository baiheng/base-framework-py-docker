#!/bin/bash
#===============================================================================
#
#          FILE:  build-docker.sh
# 
#         USAGE:  ./build-docker.sh 
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
#       CREATED:  2018年06月06日 18时49分48秒 CST
#      REVISION:  ---
#===============================================================================

docker build -t alert-center:v1 .
