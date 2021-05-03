#!/bin/bash
#Скрипт для подсчета общего количества запросов
#variables
LOGFILE="../../logs/access.log"
echo "Count Requests:"
wc $LOGFILE | awk '{print $1}'
