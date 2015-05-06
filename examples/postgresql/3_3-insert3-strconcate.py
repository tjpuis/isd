# -*- coding:UTF-8 -*-

import psycopg2

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="examdb", user="dbo", password="pass")

cur = conn.cursor()

for i in range(10):
    sn = 1001 + i
    name = 'test-%d' % sn
    name = "'); DELETE FROM test_tbl1; SELECT ('"
    sql_str = "INSERT INTO test_tbl1 (sn, name) VALUES (%d, '%s')"
    sql_str = sql_str % (sn, name)

    print(sql_str)
    cur.execute(sql_str)

conn.commit()

