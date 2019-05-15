from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=30,verbose_name='书名')
    pub_date=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名')
    # gender=models.BooleanField(default=True)
    gender = models.CharField(choices=[('man','男'),('woman','女')],max_length=10,verbose_name='性别')
    skill=models.CharField(max_length=40,null=True,verbose_name='技能')
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='来自')

    def __str__(self):
        return self.name
