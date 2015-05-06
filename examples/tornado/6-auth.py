# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

main_page = """
<html>
<body>
用户<b>%(user)s</b>登录成功
<div><a href="/logout">注销登录</a>
</div>
</body>
</html>
"""

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return

        user = tornado.escape.xhtml_escape(self.current_user)
        page = main_page % dict(user=user)
        self.write(page)

login_page = """
<html>
<body>
    <form action="/login" method="post">
    用户：<input type="text" name="userid"><br>
    密码：<input type="password" name="passwd">
    <input type="submit" value="登录">
    </form>
    <div style="color:red;">%(errmsg)s</div>
</body>
</html>
"""

# 密码表
user_passwds = { 'zhang' : 'zhangpwd', 'wang' : 'wangpwd' }

class LoginHandler(BaseHandler):
    def get(self):
        page = login_page % dict(errmsg='')
        self.write(page)

    def post(self):
        userid = self.get_argument('userid')
        passwd = self.get_argument('passwd')

        # 检查输入的密码和密码表的密码是否一致
        if passwd != user_passwds.get(userid, None):
            page = login_page % dict(errmsg='验证失败')
            self.set_status(403) # 设置状态码
            self.write(page)
            return

        # 验证成功，利用cookie设置已验证的用户信息
        self.set_secure_cookie("user", userid)
        self.redirect("/")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user") # 从cookie清除用户痕迹
        self.redirect("/")

        
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    ], 
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")

if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start()

