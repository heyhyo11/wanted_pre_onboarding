from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter

from .serializers import PostCreateSerializer, PostPutSerializer, PostGetSerializer, PostDetailSerializer, \
    ApplicationSerializer
from .models import Post, Application


# 4-2. 채용공고 검색기능 구현
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostGetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['company_id__company_name', 'company_id__country', 'company_id__region', 'position', 'prize', 'skill']


class PostsAPIView(APIView):
    # 4-1. 채용공고 목록을 가져옵니다.
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostGetSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 1. 채용공고를 등록합니다.
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PostAPIView(APIView):
    # 05. 채용 상세페이지 가져옵니다.
    def get(self, request, pk):
        post = get_object_or_404(Post, post_id=pk)
        serializer = PostDetailSerializer(post)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 02. 채용공고를 수정합니다.
    def put(self, request, pk):
        post = get_object_or_404(Post, post_id=pk)
        serializer = PostPutSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 03. 채용공고를 삭제합니다.
    def delete(self, request, pk):
        post = get_object_or_404(Post, post_id=pk)
        post.delete()
        return Response({"message": '삭제완료!'}, status=status.HTTP_200_OK)

# 06. 사용자는 채용공고에 지원합니다.
class ApplicationAPIGenerics(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer