from rest_framework import serializers
from .models import Post, Company, Application


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
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company_id.company_name

    def get_country(self, obj):
        return obj.company_id.country

    def get_region(self, obj):
        return obj.company_id.region

    class Meta:
        model = Post
        fields = ['post_id', 'company_name', 'country', 'region', 'position', 'prize', 'skill']


# 사용자 채용공고 상세조회
class PostDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    other_posts = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company_id.company_name

    def get_country(self, obj):
        return obj.company_id.country

    def get_region(self, obj):
        return obj.company_id.region

    # 다른 채용공고 리스트 확인
    def get_other_posts(self, obj):
        company_id = obj.company_id.company_id
        posts = Post.objects.filter(company_id=company_id)
        posts_id = []
        for post in posts:
            posts_id.append(post.post_id)
        return posts_id

    class Meta:
        model = Post
        fields = ['post_id', 'company_name', 'country', 'region', 'position', 'prize', 'skill', 'content', 'other_posts']

# 채용공고 지원
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['post_id', 'user_id']