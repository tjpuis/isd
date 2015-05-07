# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


html_tmpl = """
<html>
<body>
<form action="/" method="post">
  <input type="text" name="message">
  <input type="submit" value="提交消息">
</form>
<div><b>消息：</b><br>%(msg)s
</body>
</html>
"""

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        page = html_tmpl % dict(msg='<无>')
        self.write(page)

    def post(self):
        page = html_tmpl % dict(msg=self.get_argument("message"))
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write(page)


handlers = [
    (r"/", MainHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
