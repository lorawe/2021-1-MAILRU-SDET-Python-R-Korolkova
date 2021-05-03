#!/bin/bash
#variables
LOGFILE="../../logs/access.log"
RESULTFILE="../../results/bash_result.txt"
#Скрипт для подсчета общего количества запросов, считает по строкам
echo "Count Requests:" > $RESULTFILE
wc $LOGFILE | awk '{print $1}' >> $RESULTFILE
#Скрипт для подсчета количества запросов по методам
echo "=====================" >> $RESULTFILE
echo "Count Requests with Methods:" >> $RESULTFILE
cat $LOGFILE | grep "GET" | wc | awk '{print "GET - "$1}' >> $RESULTFILE
cat $LOGFILE | grep "POST" | wc | awk '{print "POST - "$1}' >> $RESULTFILE
cat $LOGFILE | grep "PUT" | wc | awk '{print "PUT - "$1}' >> $RESULTFILE
cat $LOGFILE | grep "DELETE" | wc | awk '{print "DELETE - "$1}' >> $RESULTFILE
#Скрипт для выявления 10 самых частых запросов
echo "=====================" >> $RESULTFILE
echo "Top 10 Request Pages:" >> $RESULTFILE
cat $LOGFILE | awk '{print $7}' | sort | uniq -c | sort -nr | awk '{print $1, $2}' | head -10 >> $RESULTFILE
#Скрипт для выявления 5 самых тяжелых запросов 4XX
echo "=====================" >> $RESULTFILE
echo "Top 5 Request with Heavy 4XX:" >> $RESULTFILE
cat  $LOGFILE | awk '{if ($9 >= 400 && $9 < 500) print $7, $9, $10, $1}'| sort -nr -k 3 | head -5 >> $RESULTFILE
#Скрипт для нахождения 5 пользователей по количеству запросов со статусом 5XX
echo "=====================" >> $RESULTFILE
echo "Top 5 Users with 5XX:" >> $RESULTFILE
cat  $LOGFILE | awk '{if ($9 >= 500 && $9 < 600) print $1}' | sort | uniq -c | sort -nr | awk '{print $1, $2}' | head -5 >> $RESULTFILE
