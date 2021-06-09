#!/bin/bash
mysql "-uroot" -p < "/etc/appconfig/db/create_table_and_user.sql"
${MYSQL_ROOT_PASSWORD}