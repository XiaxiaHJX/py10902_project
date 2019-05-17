from django.db import models

# Create your models here.

#定义标题
class VoteHeadline(models.Model):
    title=models.CharField(max_length=50,)
    def __str__(self):
        return self.title

#定义选项1
class VoteOption_1(models.Model):
    optionname=models.CharField(max_length=50,)
    num=models.BigIntegerField(max_length=11,)
    head=models.ForeignKey(VoteHeadline,on_delete=models.CASCADE())
    def __str__(self):
        return self.optionname

#定义选项2
class VoteOption_2(models.Model):
    optionname = models.CharField(max_length=50,)
    num = models.BigIntegerField(max_length=11, )
    head = models.ForeignKey(VoteHeadline, on_delete=models.CASCADE())
    def __str__(self):
        return self.optionname

