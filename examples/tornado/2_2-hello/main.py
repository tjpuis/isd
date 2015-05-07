# -*- coding: utf-8 -*-

import tornado.web

# HTTP请求处理器(HTTP Request Handler)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world1") 

# ----------------------------------------------------
# Web服务应用

# HTTP请求派发处理器定义
handlers = [ 
    (r"/", MainHandler), 
]

settings = {'debug' : True}
application = tornado.web.Application(handlers, **settings)
application.listen(8888) # 监听8888端口 


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度

