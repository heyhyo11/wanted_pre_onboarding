from django.urls import path

from post.views import PostsAPIView, PostAPIView, PostListView, ApplicationAPIGenerics

urlpatterns = [
    path('posts/', PostsAPIView.as_view()),
    path('posts/search/', PostListView.as_view()),
    path('post/<int:pk>/', PostAPIView.as_view()),
    path('application/', ApplicationAPIGenerics.as_view()),
]