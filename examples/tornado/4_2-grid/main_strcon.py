# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n, m = 5, 4
        title = '网格(%d x %d)' % (n, m)

        self.write("""
        <html>
        <head>
        <title>%s</title>
        </head>
        <body>
        """ % title)


        self.write("""
        <h3>%s</h3>
        <table border='1'>
        <tbody>
        """ % title)

        for i in range(n):
            self.write('<tr>\n')
            for j in range(m):
                if i == j :
                    self.write('<td style="color:red">')
                else:
                    self.write('<td>')
                self.write('(%d, %d)' % (i, j))
                self.write('</td>')
            self.write('</tr>\n')
        
        self.write("""
        </tbody></table>
        </body></html>
        """)

handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
