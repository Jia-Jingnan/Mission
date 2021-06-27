from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
# 针对模型的测试：测试增删改查
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



# 运行测试时不会真的调用数据库，会创建一个独立的环境，不会在开发环境生成垃圾数据
