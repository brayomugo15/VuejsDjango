from django.urls import path
from news.api.views import article_list_create_api_list

urlpatterns = [
    path("articles/", article_list_create_api_list, name="article-list")
]
