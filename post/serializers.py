from rest_framework import serializers
from .models import Post, Company


# 회사 시리얼라이저
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


# 채용공고 생성
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['company_id', 'position', 'prize', 'content', 'skill']


# 채용공고 수정
class PostPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['position', 'prize', 'content', 'skill']


# 사용자 채용공고 전체 조회
class PostGetSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()
    class Meta:
        model = Post
        fields = ['post_id', 'company_id', 'position', 'prize', 'skill']


# 사용자 채용공고 조회
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id', 'position', 'prize', 'skill']

