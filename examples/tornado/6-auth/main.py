# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        # 重载RequestHandler函数，以便子类可以使用current_user属性得到合法用户的标识
        # 如果当前用户没有验证，则没有相应的cookie，因此返回的是None
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):

    """首页处理器"""
    def get(self):

        # 如果没有合法用户存在，则重定向到登录页面，要求用户登录
        if not self.current_user:
            self.redirect("/login") # 重定向到登录页面
            return

        user_id = tornado.escape.xhtml_escape(self.current_user)
        self.render("web/main.html", user_id=user_id)

class LoginHandler(BaseHandler):
    """登录处理器"""

    def get(self):
        """绘制登录页面"""
        self.render("web/login.html", errmsg=None)

    def post(self):
        """验证登录表单录入的用户名和密码是否一致"""

        userid = self.get_argument('userid')
        passwd = self.get_argument('passwd')

        # 检查输入的密码和密码表的密码是否一致
        if passwd != user_passwds.get(userid, None):
            self.render("web/login.html", errmsg='验证失败')
            self.set_status(403) # 设置状态码
            return

        # 验证成功，利用cookie设置已验证的用户信息
        self.set_secure_cookie("user", userid)
        self.redirect("/") # 验证成功，重定向到首页

class LogoutHandler(BaseHandler):
    """注销登录请求的处理器"""
    def get(self):
        # 清除含有用户信息的cookie，即为注销登录
        self.clear_cookie("user") 
        self.redirect("/")

# 密码表
user_passwds = { 'zhang' : 'zhangpwd', 'wang' : 'wangpwd' }


handlers = [
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
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


