from django.contrib import admin
from django.urls import path, include

from article.views import ArticleForAll, PrivateArticle, AuthorArticle, ArticleCreat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/article_for_other/', ArticleForAll.as_view(), name='all_article'),
    path('api/v1/article_for_subscriber/', PrivateArticle.as_view(), name='subscriber_article'),
    path('api/v1/article/<int:pk>', AuthorArticle.as_view(), name='detail_article'),
    path('api/v1/article_creat', ArticleCreat.as_view(), name='create'),
]
