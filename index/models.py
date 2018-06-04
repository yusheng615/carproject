from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30,verbose_name='用户名')
    pwd = models.CharField(max_length=100,verbose_name='密码')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    isactive = models.BooleanField(default=True,verbose_name='激活状态')

