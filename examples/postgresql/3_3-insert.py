# -*- coding:UTF-8 -*-

import psycopg2

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="examdb", user="dbo", password="pass")

cur = conn.cursor()

ins_sql = 'INSERT INTO test_tbl1 (sn, name) VALUES (%s, %s)'
for i in range(10):
    sn = 1001 + i
    name = 'test-%d' % sn
    cur.execute(ins_sql, (sn, name) )

conn.commit()

