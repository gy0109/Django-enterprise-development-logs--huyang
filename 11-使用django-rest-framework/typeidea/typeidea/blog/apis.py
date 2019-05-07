from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@api_view()    # api_view 快速提供api接口  [’GET', 'POST]指定方法
def post_list(request):
    posts = Post.objects.filter(status=Post.STATUS_NORMAL)
    post_serializers = PostSerializer(posts, many=True)
    return Response(post_serializers.data)


# ListCreateAPIView 和LISTView类似  需要提供queryset参数  数据列表页
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer



