#! /usr/bin/env python3

import pyodbc

dsn='PortriskSynapse'
db='portrisk_synapse_workspace_sql_pool'
user='sqladminuser'
pwd='PortriskSqlPool!'


connStr='DSN={}; UID={}; PWD={}'.format(dsn, user, pwd)
print(connStr)
conn=pyodbc.connect(connStr)

cursor = conn.cursor()
cursor.execute('SELECT * from dbo.exp')

for row in cursor:
    print(row)
