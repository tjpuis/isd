
import psycopg2
import psycopg2.pool

dbconn_pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=2, maxconn=10,
    host='localhost', database='examdb',
    user='dbo', password='pass')

from contextlib import contextmanager
@contextmanager
def db_cursor():
    conn = dbconn_pool.getconn()
    try:
        with conn.cursor() as cur:
            yield cur
            conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        dbconn_pool.putconn(conn)


with db_cursor() as cur :
    s = 'SELECT * from course'
    cur.execute(s)
    for r in cur:
        print(r)
