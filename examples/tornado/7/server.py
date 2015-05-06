# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["路人甲", "路人乙", "路人丙"]
        self.render("list.html", title="这是标题", items=items)

# 以本程序文件所在的目录，作为服务根目录
home_path = os.path.dirname(__file__)

settings = {
    "static_path": os.path.join(home_path, "static"),
    "debug": "true"
}

application = tornado.web.Application([
    (r"/", MainHandler)
    ], **settings)

if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

