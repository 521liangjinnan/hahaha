# 导包
import unittest

# 创建测试类
import requests


class TestTpShopLogin(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        # 获取session对象
        cls.session = requests.session()
        # 定义
        cls.url_code = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        cls.url_login = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    # 登陆成功
    def test01_login_success(self):
        self.session.get(self.url_code)
        # 请求登录
        data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        r = self.session.post(url=self.url_login, data=data)
        # 断言
        self.assertEqual(1, r.json().get("status"))
        print(r.json())

    # 账号不存在
    def test02_username_err(self):
        self.session.get(self.url_code)
        # 请求登录
        data = {"username": "13800001111", "password": "123456", "verify_code": "8888"}
        r = self.session.post(url=self.url_login, data=data)
        # 断言
        self.assertEqual(-1, r.json().get("status"))
        print(r.json())

    # 密码错误
    def test03_pwd_err(self):
        self.session.get(self.url_code)
        # 请求登录
        data = {"username": "13012345678", "password": "1234567", "verify_code": "8888"}
        r = self.session.post(url=self.url_login, data=data)
        # 断言
        self.assertEqual(-2, r.json().get("status"))
        print(r.json())
