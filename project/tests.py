from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from project.models import Project


# Create your tests here.
class ProjectTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('thor', 'thor@gmail.com', 'thor')
        # 添加项目数据
        Project.objects.create(name='Coles', describe='Coles Online')
        self.client = Client()
        data = {'username': 'thor', 'password': 'thor'}
        response = self.client.post('/login/', data)

    def test_project_list(self):
        response = self.client.get('/project/list/')
        project_list_html = response.content.decode('utf-8')
        print(project_list_html)
        self.assertEqual(response.status_code , 200)
        # 是否包含新增加的项目
        self.assertIn('Coles', project_list_html)