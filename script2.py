#!/usr/bin/python

import subprocess

TARGET_FILE="/home/karthikeyankrishnasw/USERSFILE.sql"
ADMIN_USER="***"
ADMIN_PASS="***"
SID="ORCL"
PROTO="TCP"
HOSTNAME="***"
PORT="1521"
USERS="/home/karthikeyankrishnasw/properties.txt"

open(TARGET_FILE, "w").close()

with open(USERS, r) as f:
	var = f.readlines()
for i in var:
        j=i.split(":")
        USER=j[0]
        PASS=j[1]
        str1 = "create user %s identified by %s profile ORA_STIG_PROFILE default tablespace users quota unlimited on users temporary tablespace temp password expire" % (USER,PASS)
        with open(TARGET_FILE, "a") as g:
        	g.write(str1 + "\n")
        str2 = "grant DBA to %s with admin option" % (USER)
        with open(TARGET_FILE, "a") as g:
        	g.write(str2 + "\n")

def run_DBAuser_schema():
	"""try subprocess with sqlplus and TARGET_FILE"""
