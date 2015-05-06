# -*- coding: utf-8 -*-

import tornado.web


html_tmpl = """
<html>
<body>
<form action="/" method="get">
  <input type="text" name="message">
  <input type="submit" value="提交消息">
</form>
<div><b>消息：</b><br>%(msg)s
</body>
</html>
"""

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        msg = self.get_argument("message", None)
        if msg is None:
            msg = '<无>'

        page = html_tmpl % dict(msg=msg)

        self.set_header("Content-Type", "text/html;charset=utf-8")
        self.write(page)


application = tornado.web.Application([
    (r"/", MainHandler)
])

if __name__ == "__main__":
    application.listen(8888) # 服务监听8888端口

    # 启动调度程序
    import tornado.ioloop    
    server = tornado.ioloop.IOLoop.instance()
    # 添加一个周期性的空事件，以便可以及时捕捉CTRL-C终端程序
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

