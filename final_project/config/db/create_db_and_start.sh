#!/bin/bash
mysql -h"percona" "-uroot" "-pMYSQL_CONTAINER_SDET_MAIL_PASS" < "/etc/appconfig/db/create_table_and_user.sql"
/app/myapp "--config=/etc/appconfig/config"