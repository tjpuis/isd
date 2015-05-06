# -*- coding:UTF-8 -*-

import psycopg2

# Connect to an existing database


conn = psycopg2.connect(host='localhost', 
	database="examdb", user="dbo", password="pass")

cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS test_tbl1;
CREATE TABLE IF NOT EXISTS test_tbl1  (
    sn       INTEGER,    --序号
    name     TEXT        --姓名
);
''')

conn.commit()

