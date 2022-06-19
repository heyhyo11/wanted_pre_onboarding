from django.contrib import admin

# Register your models here.
from post.models import Post, Company, User

admin.site.register(Post)
admin.site.register(Company)
admin.site.register(User)