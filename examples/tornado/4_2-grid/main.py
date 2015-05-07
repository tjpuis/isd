# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("grid.html", n=5, m=4)

handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
