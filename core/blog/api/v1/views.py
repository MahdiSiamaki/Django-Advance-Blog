from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from ...models import Post, Category
from .paginations import DefaultPagination
from rest_framework import status


"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

'''class PostList(APIView):
    """List all posts or create a new post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request):
        """List all posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        """Create a new post"""
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)'''

'''class PostList(ListCreateAPIView):
    """List all posts or create a new post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
'''

"""@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'Post deleted'},status=status.HTTP_204_NO_CONTENT)"""

'''class PostDetail(APIView):
    """Retrieve, update or delete a post instance"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self,request,pk):
        """Retrieve a post"""
        post = get_object_or_404(Post,pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self,request,pk):
        """Update a post"""
        post = get_object_or_404(Post,pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        """Delete a post"""
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        return Response({'detail':'Post deleted'},status=status.HTTP_204_NO_CONTENT)'''


'''class PostDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a post instance"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    lookup_url_kwarg = 'pk'
    lookup_field = 'pk'
    # lookup_field = 'id'
    # lookup_url_kwarg = 'id'
'''


class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_at"]
    pagination_class = DefaultPagination
    lookup_url_kwarg = "pk"
    lookup_field = "pk"


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
