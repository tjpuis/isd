# -*- coding:UTF-8 -*-

import psycopg2

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="examdb", user="examdbo", password="pass")

cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS test_tbl1;
CREATE TABLE IF NOT EXISTS test_tbl1  (
    sn       INTEGER,    --序号
    name     TEXT        --姓名
);
	''')

for i in xrange(10):
	sn = 1001 + i
	name = 'test-%d' % sn
	cur.execute('''
		INSERT INTO test_tbl1 (sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':sn, 'name':name} )

conn.commit()

