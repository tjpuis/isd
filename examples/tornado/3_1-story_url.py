# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write('''<html><body>
            <ul><li><a href='/story/1001'>故事1</a></li>
            <li><a href='/story/1002'>故事2</a></li></ul>
            </body></html>''')

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.set_header("Content-Type", "text/plain; charset=utf-8")
        self.write("阅读故事 " + story_id + "")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    # 启动调度程序
    import tornado.ioloop    
    server = tornado.ioloop.IOLoop.instance()
    # 添加一个周期性的空事件，以便可以及时捕捉CTRL-C终端程序
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()
