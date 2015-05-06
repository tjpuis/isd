# -*- coding: utf-8 -*-


import tornado.web

# HTTP请求处理器(HTTP Request Handler)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

# Web服务应用
application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888) # 服务监听8888端口

    # 启动调度程序
    import tornado.ioloop    
    server = tornado.ioloop.IOLoop.instance()
    # 添加一个周期性的空事件，以便可以及时捕捉CTRL-C终端程序
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()


    
