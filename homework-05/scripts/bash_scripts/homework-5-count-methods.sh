#!/bin/bash
#Скрипт для подсчета количества запросов по методам
#variables
LOGFILE="../../logs/access.log"
echo "Count Requests with Methods:"
cat $LOGFILE | grep "GET" | wc | awk '{print "GET - "$1}'
cat $LOGFILE | grep "POST" | wc | awk '{print "POST - "$1}'
cat $LOGFILE | grep "PUT" | wc | awk '{print "PUT - "$1}'
cat $LOGFILE | grep "DELETE" | wc | awk '{print "DELETE - "$1}'
