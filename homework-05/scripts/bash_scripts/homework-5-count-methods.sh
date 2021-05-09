#!/bin/bash
#Скрипт для подсчета количества запросов по методам
#variables
LOGFILE="../../logs/access.log"
METHODS="GET PUT POST HEAD DELETE CONNECT OPTIONS TRACE PATCH"
echo "Count Requests with Methods:"
cat $LOGFILE | awk '{print $6}' | cut -d'"' -f2 | awk -v methods="$METHODS" 'BEGIN {
														split(methods, methodsAsValues)
														for (i in methodsAsValues) methodsAsKeys[methodsAsValues[i]] = ""
														} 
														{if ($1 in methodsAsKeys) {print $1} else {print "Некорректный запрос: " $1}}' | sort | uniq -c | sort -nr -k 1
