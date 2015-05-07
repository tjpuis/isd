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

handlers = [
    (r"/", MainHandler),
]

# 使用secure_cookie，需要对传输的cookie内容进行加密，
# 因此需要预先设置加密的密钥
settings = dict(
    cookie_secret="_此处为应为随机生成的密钥_", 
    debug=True)
application = tornado.web.Application(handlers, **settings)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
