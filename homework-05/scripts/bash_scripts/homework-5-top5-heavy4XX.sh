#!/bin/bash
#Скрипт для выявления 5 самых тяжелых запросов 4XX
#variables
LOGFILE="../../logs/access.log"
echo "Top 5 Request with Heavy 4XX:"
cat  $LOGFILE | awk '{if ($9 >= 400 && $9 < 500) print $7, $9, $10, $1}'| sort -nr -k 3 | head -5
