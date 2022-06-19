from django.urls import path

from post.views import PostsAPI

urlpatterns = [
    path('posts/', PostsAPI.as_view()),
]