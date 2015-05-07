# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("count_cookie"):
            self.set_cookie("count_cookie", "0")
            self.write("刚设置了Cookie!，计数为0")
            
        else:
            count = int(self.get_cookie("count_cookie")) + 1
            self.set_cookie("count_cookie", str(count))
            self.write("你的Cookie, 当前计数: %d" % count)

handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
