from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
# 模版Template测试导入的相关的包
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome


# Create your tests here.
# 针对模型的测试：测试增删改查
# 运行测试时不会真的调用数据库，会创建一个独立的环境，不会在开发环境生成垃圾数据
class UserTestCase(TestCase):

    # 初始化
    def setUp(self):
        # 创建一个用户
        User.objects.create_user('thor', 'thor@asgard.com', 'thor')

    # 测试用例
    def test_select_user(self):
        # 查询用户信息，断言
        user = User.objects.get(username='thor')
        self.assertEqual(user.username, 'thor')

    def test_add_user(self):
        User.objects.create_user('loki', 'loki@asgard.com', 'loki')
        user = User.objects.get(username='loki')
        self.assertEqual(user.email, 'loki@asgard.com')

    def test_update_user(self):
        user = User.objects.get(username='thor')
        user.username = 'God of Thunder'
        user.save()
        self.assertEqual(user.username, 'God of Thunder')

    def test_delete_user(self):
        user = User.objects.get(username='thor')
        user.delete()
        users = User.objects.all()
        print('users的长度为：',len(users))
        self.assertEqual(len(users), 0)


# 针对视图的测试
class IndexTestCase(TestCase):

    def setUp(self):
        # 初始化一个client
        self.client = Client()


    def test_index(self):
        response = self.client.get("/")
        # 打印出html页面
        print('index响应内容为：', response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # 断言Template模版是否有用到
        self.assertTemplateUsed(response, 'index.html')


class LoginTestCase(TestCase):

    def setUp(self):
        # 初始化一个client
        self.client = Client()
        # 创建用户,后续登陆使用
        User.objects.create_user('thor', 'thor@asgard.com', 'thor')

    # 用户名密码为空
    def test_login_null(self):
        data = {'username': '', 'password': ''}
        response = self.client.post('/login/', data)
        # 转成html页面
        html_res = response.content.decode('utf-8')
        print(html_res)
        print(response)
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'index.html')
        self.assertIn('用户名或密码错误', 'index.html')

    # 用户名密码错误
    def test_login_null(self):
        data = {'username': 'admin', 'password': 'admin1'}
        response = self.client.post('/login/', data)
        # 转成html页面
        html_res = response.content.decode('utf-8')
        print(html_res)
        print(response)
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'index.html')
        self.assertIn('用户名或密码错误', 'index.html')

    # 正确用户名密码
    def test_login_null(self):
        data = {'username': 'thor', 'password': 'thor'}
        response = self.client.post('/login/', data)
        # 转成html页面
        html_res = response.content.decode('utf-8')
        print(html_res)
        print(response)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'index.html')


class LogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # 创建用户,后续登陆使用
        User.objects.create_user('thor', 'thor@asgard.com', 'thor')
        # 登陆
        data = {'username': 'thor', 'password': 'thor'}
        response = self.client.post('/login/', data)

    def test_logout(self):
        response = self.client.get('/logout/')
        html_res = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 302)


# 针对模版Template测试
class LoginTemplateTestCase(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitlu_wait(10)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        super.tearDownCase()


    def test_login_template(self):
        self.driver.get('%s%s'%(self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys('')
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys('')
        # sleep(1)

        self.driver.find_element_by_id('login').click()
        tips = self.driver.find_element_by_id('error')
        print(tips)
        self.assertEqual(tips, '用户名或密码为空')
        # sleep()
