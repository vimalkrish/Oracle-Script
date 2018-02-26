#!/usr/bin/python

import subprocess
from sqlplus_commando import SqlplusCommando

TARGET_FILE="/home/karthikeyankrishnasw/USERSFILE.sql"
ADMIN_USER="*****"
ADMIN_PASS="*****"
SID="ORCL"
PROTO="TCP"
HOSTNAME="******"
PORT="1521"
USERS="/home/karthikeyankrishnasw/properties.txt"

open(TARGET_FILE, "w").close()

with open(USERS, r) as f:
	var = f.readlines()
for i in var:
        j=i.split(":")
        USER=j[0]
        PASS=j[1]
        str1 = "create user %s identified by %s profile ORA_STIG_PROFILE default tablespace users quota unlimited on users temporary tablespace temp password expire;" % (USER,PASS)
        str2 = "grant DBA to %s with admin option;" % (USER)
        sqlplus = SqlplusCommando(hostname=HOSTNAME, database=SID, username=ADMIN_USER, password=ficodatabase)
        result1 = sqlplus.run_query("%s" % str1)
        result2 = sqlplus.run_query("%s" % str2)
        print result1
        print result2
