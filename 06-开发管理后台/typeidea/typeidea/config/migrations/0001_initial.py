# Generated by Django 2.1.7 on 2019-04-27 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='')),
                ('href', models.URLField(verbose_name='链接')),
                ('status', models.PositiveIntegerField(choices=[('STATUS_NORMAL', '正常'), ('STATUS_DELETE', '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('weight', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重高展示顺序靠前', verbose_name='权重')),
                ('owner', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链',
            },
        ),
        migrations.CreateModel(
            name='SiderBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('display_type', models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论')], default=1, verbose_name='展示类型')),
                ('content', models.CharField(blank=True, help_text='如果设置的不是HTML类型，可为空', max_length=500, verbose_name='内容')),
                ('status', models.PositiveIntegerField(choices=[('STATUS_SHOW', '展示'), ('STATUS_HIDE', '隐藏')], default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '侧边栏',
                'verbose_name_plural': '侧边栏',
            },
        ),
    ]
