from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Article
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer


class ArticleForAll(generics.ListAPIView):
    queryset = Article.objects.filter(category_id=3)
    serializer_class = ArticleSerializer


class PrivateArticle(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class AuthorArticle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ArticleCreat(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (DjangoModelPermissions,)
