#!/bin/bash
#Скрипт для нахождения 5 пользователей по количеству запросов со статусом 5XX
#variables
LOGFILE="../../logs/access.log"
echo "Top 5 Users with 5XX:"
cat  $LOGFILE | awk '{if ($9 >= 500 && $9 < 600) print $1}' | sort | uniq -c | sort -nr | awk '{print $2, $1}' | head -5
