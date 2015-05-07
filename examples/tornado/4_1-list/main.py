# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["路人甲", "路人乙", "路人丙"]
        self.set_header("Content-Type", "text/html")
        self.render("list.html", title="这是标题", items=items)

handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
