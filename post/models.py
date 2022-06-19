from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField('채용공고_id', primary_key=True)
    company_id = models.ForeignKey('Company', related_name='company',
                                   on_delete=models.CASCADE, db_column='company_id')
    position = models.CharField('채용포지션', max_length=100)
    prize = models.IntegerField('채용보상금')
    content = models.TextField('채용내용')
    skill = models.CharField('사용기술', max_length=100)

    def __str__(self):
        return 'post_id: {0} / company_id: {1}'.format(self.post_id, self.company_id)


class Company(models.Model):
    company_id = models.IntegerField('회사_id', primary_key=True)
    company_name = models.CharField('회사명', max_length=50)
    country = models.CharField('국가', max_length=50)
    region = models.CharField('지역', max_length=50)

    def __str__(self):
        return '{0}: {1}'.format(self.company_id, self.company_name)


class User(models.Model):
    user_id = models.IntegerField('사용자_id', primary_key=True)
    user_name = models.CharField('사용자명', max_length=20)

    def __str__(self):
        return '{0}: {1}'.format(self.user_id, self.user_name)


class Apply(models.Model):
    post_id = models.ForeignKey('Post', related_name='post',
                                   on_delete=models.CASCADE, db_column='post_id')
    user_id = models.ForeignKey('User', related_name='user',
                                   on_delete=models.CASCADE, db_column='user_id')

