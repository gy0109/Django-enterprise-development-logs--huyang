from rest_framework import serializers, pagination

from .models import Post, Category


# http://127.0.0.1:8000/api/post/     (?format=json)
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
    # created_time = serializers.DateTimeField(
    #     format="%Y%-%m-%d %H:%M:%S"
    # )

    # SlugRelatedField: 通常用来定义外键
    # read_only  是否可写
    # 多对多指定many参数
    # slug_field指定显示什么

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner',  'created_time']


# http://127.0.0.1:8000/api/post/11/
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content_html', 'created_time']


# http://127.0.0.1:8000/api/category/
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_time']


# http://127.0.0.1:8000/api/category/3/   分类详情页
class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')
    # SerializerMethodField paginated_posts方法  在最终返回的数据里 posts对应的数据需要通过 paginated_posts来获取

    # 分页
    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page,
                                    many=True,
                                    context={'request': self.context['request']}
                                    )
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_time', 'posts')


