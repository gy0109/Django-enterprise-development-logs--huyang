from django.test import TestCase, Client

from .models import Student
# Create your tests here.
"""
TestCase的方法简介：
setUp: 用来初始化环境，包括创建初始化数据，做一些准备工作
test_xxxx: 系统会认为是需要测试的方法， 跑测试的时候  会被执行， 每个测试方法时相互独立的  
teardown: 与setUP相对 清理测试环境和测试数据  （不管）

"""


class StudentTestCase(TestCase):
    def setUp(self):
        # 初始化一些信息 创建初始化的数据
        Student.objects.create(
            name='刘清爽',
            sex=2,
            email='liuqingshuang@163.com',
            profession='hr',
            qq='4567798900',
            phone='13789572356'
        )

    def test_create_and_sex_show(self):
        # 测试   添加数据并且显示sex
        student = Student.objects.create(
            name='刘俊龙',
            sex=1,
            email='liujunlong@163.com',
            profession='hr',
            qq='423533342900',
            phone='13748379823'
        )

        # sex_show()    可以更换为  get_sex_display  仅针对于choices的字段
        self.assertEqual(student.sex_show, '男', '性别字段内容与展示不一样')

    def test_filter(self):
        # 测试filter
        Student.objects.create(
            name='刘清爽',
            sex=2,
            email='liuqingshuang@163.com',
            profession='hr',
            qq='4567798900',
            phone='13789572356'
        )
        name = '刘清爽'
        student = Student.objects.filter(name=name)   # 这个返回一个列表
        self.assertEqual(len(student), 1, '应该只能存在一个姓名为{}的记录'.format(name))

    def test_get_index(self):
        # 请求首页
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200！')

    def test_post_student(self):
        # 提交数据 然后请求首页 查看数据是否存在
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='liung@163.com',
            profession='程序员',
            qq='4567798900',
            phone='13789572356'
        )

        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertEqual(b'test_for_post' in response.content, 'response content must contain "test_for_post"')


