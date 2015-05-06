# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("count_cookie"):
            self.set_secure_cookie("count_cookie", "0")
            self.write("刚设置了Cookie!，计数为0")
            
        else:
            count = int(self.get_secure_cookie("count_cookie")) + 1
            self.set_secure_cookie("count_cookie", str(count))
            self.write("你的Cookie, 当前计数: %d" % count)

application = tornado.web.Application([
    (r"/", MainHandler)
    ],
    cookie_secret="__TODO:_随机生成的密钥__", 
    debug=True)

if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

