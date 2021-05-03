#!/bin/bash
#Скрипт для выявления 10 самых частых запросов
#variables
LOGFILE="../../logs/access.log"
echo "Count Requests:"
cat $LOGFILE | echo "Top 10 Request Pages:" | echo "=====================" | awk '{print $7}' | sort | uniq -c | sort -nr | awk '{print $1, $2}' | head -10
