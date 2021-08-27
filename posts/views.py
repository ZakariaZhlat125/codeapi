from rest_framework import generics,permissions
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Post
from .pernissions import IsAuthOrReadOnly
from .Serializers import PostSerializer,UserSerializer
class PostViewSet(viewsets.ModelViewSet):
    permission_class=(IsAuthOrReadOnly)
    queryset=Post.objects.all()
    serializers_class=PostSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializers_class=PostSerializer
class PostList(generics.ListCreateAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserList(generics.ListCreateAPIView):
    queryset=get_user_model().objects.all()
    serializer_class =UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=get_user_model().objects.all()
    serializer_class =UserSerializer