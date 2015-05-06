# -*- coding:UTF-8 -*-

import psycopg2

conn = psycopg2.connect(host='localhost', 
	database="examdb", user="dbo", password="pass")


with conn.cursor() as cur:
    sql = '''
    SELECT s.name, c.name, g.grade 
    FROM course_grade as g
        LEFT OUTER JOIN student as s ON g.stu_sn = s.sn
        LEFT OUTER JOIN course as c  ON g.cou_sn = c.sn ;
    '''
    cur.execute(sql)

    for row in cur:
        print('%s, %s, %f' % (row[0], row[1], row[2]))

conn.commit()

