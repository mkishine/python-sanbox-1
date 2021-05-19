#! /usr/bin/env python3

import pyodbc
import keyring

dsn='PortriskSynapse'
db='portrisk_synapse_workspace_sql_pool'
user='sqladminuser'
pwd=keyring.get_password("synapse", user)


connStr='DSN={}; UID={}; PWD={}'.format(dsn, user, pwd)
conn=pyodbc.connect(connStr)

cursor = conn.cursor()
cursor.execute('SELECT * from dbo.exp')

for row in cursor:
    print(row)
