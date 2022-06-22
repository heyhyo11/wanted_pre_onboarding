from django.urls import path

from post.views import PostsAPIView, PostAPIView, PostListView, ApplicationAPIGenerics

urlpatterns = [
    # 채용공고 등록, 전체조회
    path('posts/', PostsAPIView.as_view()),

    # 채용공고 검색
    path('posts/search/', PostListView.as_view()),

    # 채용공고 상세페이지 조회, 수정, 삭제
    path('post/<int:pk>/', PostAPIView.as_view()),

    # 채용공고 지원
    path('application/', ApplicationAPIGenerics.as_view()),
]