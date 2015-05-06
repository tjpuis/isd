
import psycopg2
import psycopg2.pool

pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=2, maxconn=10,
    host='localhost', dbname='examdb',
    user='dbo', password='pass')

conn = pool.getconn()
try:
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
finally:
    pool.putconn(conn)

