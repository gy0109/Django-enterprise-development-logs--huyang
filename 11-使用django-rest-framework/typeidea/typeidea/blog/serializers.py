from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    created_time = serializers.DateTimeField(
        format='%Y%-%m-%d %H:%M:%S'
    )

    # SlugRelatedField: 通常用来定义外键
    # read_only  是否可写
    # 多对多指定many参数
    # slug_field指定显示什么

    class Meta:
        model = Post
        fields = ['title', 'category', 'descripition', 'content_html', 'created_time']


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content_html', 'created_time']


