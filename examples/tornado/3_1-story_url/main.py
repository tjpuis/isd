# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

main_page = """
<html><body>
<ul>
    <li><a href='/story/1001'>故事1</a></li>
    <li><a href='/story/1002'>故事2</a></li>
</ul>
</body></html>
"""

story_page = """
<html><body>
<a href="/"> 返回列表 </a>
<hr>
<h3>故事 %(story_id)s </h3>
。。。
</body></html>
"""

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write(main_page)

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        page = story_page % dict(story_id=story_id)
        self.write(page)

handlers = [
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
]
application = tornado.web.Application(handlers, debug=True)
application.listen(8888)


if __name__ == '__main__':
    import ioloop
    ioloop.run() # 服务主调度
