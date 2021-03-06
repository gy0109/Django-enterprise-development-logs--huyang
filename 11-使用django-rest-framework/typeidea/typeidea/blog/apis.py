from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Post, Category, Tag
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer


# @api_view()    # api_view 快速提供api接口  [’GET', 'POST]指定方法
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
#
# # ListCreateAPIView 和LISTView类似  需要提供queryset参数  数据列表页
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer


# 基础的数据操作接口   Post
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]   # 权限  写入

    # retrieve实现不同接口实现不同的serializer
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    # def filter_queryset(self, queryset):
    #     category_id = self.request.query_params.get('category')
    #     if category_id:
    #         queryset = queryset.filter(category_id=category_id)


# Category   读
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]   # 权限  写入

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)
