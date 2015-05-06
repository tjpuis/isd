# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["路人甲", "路人乙", "路人丙"]
        self.set_header("Content-Type", "text/html")
        self.render("list.html", title="这是标题", items=items)

application = tornado.web.Application([
    (r"/", MainHandler)
], debug=True)


if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

