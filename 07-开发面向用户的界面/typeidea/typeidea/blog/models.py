from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    # STATUS_NORMAL = 1
    # STATUS_DELETE = 0
    STATUS_ITEMS = [
        (1, '正常'),
        (0, '删除')
    ]
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_nav = models.BooleanField(default=False, verbose_name='是否导航')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    # STATUS_NORMAL = 1
    # STATUS_DELETE = 0
    STATUS_ITEMS = [
        (1, '正常'),
        (0, '删除')
    ]
    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRSFT = 2
    STATUS_ITEMS = [
        (1, '正常'),
        (0, '删除'),
        (2, '草稿')
    ]
    title = models.CharField(max_length=255, verbose_name='标题')
    descripition = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须以markdown格式')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title

    # 重构post_list视图
    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')

        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')

        return post_list, category

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=Post.STATUS_NORMAL)



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
