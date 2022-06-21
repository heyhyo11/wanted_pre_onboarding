from django.urls import path

from post.views import PostsAPIView, PostAPIView, PostListView

urlpatterns = [
    path('posts/', PostsAPIView.as_view()),
    path('posts/search/', PostListView.as_view()),
    path('post/<int:pk>/', PostAPIView.as_view()),
]