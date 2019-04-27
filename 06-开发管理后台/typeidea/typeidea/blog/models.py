from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS_NORMAL = 1
STATUS_DELETE = 0
STATUS_DRSFT = 2
STATUS_ITEMS = [
    ('STATUS_NORMAL', '正常'),
    ('STATUS_DELETE', '删除'),
    ('STATUS_DRSFT', '草稿')
]


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    creates_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_nav = models.BooleanField(default=False, verbose_name='是否导航')
    owner = models.ForeignKey(User, on_delete=True, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=True,  verbose_name='作者')
    creates_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    descripition = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须以markdown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, on_delete=True,  verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, on_delete=True,  verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']


"""
常用字段介绍：
1.数值型：
PositiveIntegerField
BooleanField
DecimalField
AutoField
SmallIntegerField


2.关系型：
ManyToManyField
ForeignKey
OneToOneField

3.日期型：
DateTimeField
DateField
TimeField

4. 字符型：
CharField
TextField
ImageField
FileField
UUIDField
EmailField
URLField
"""
