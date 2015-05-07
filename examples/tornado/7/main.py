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

handlers = [
    (r"/", MainHandler),
]

settings = {
    "static_path": os.path.join(home_path, "static"),
    "debug": "true"
}

application = tornado.web.Application(handlers, **settings)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度

