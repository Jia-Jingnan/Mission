from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


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



