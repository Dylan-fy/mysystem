# coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    SEX_CHOICES =(
        (u'男',u'boy'),
        (u'女',u'girl'),
    )
    username = models.CharField(max_length=100, verbose_name= '用户名')
    password = models.CharField(max_length=200,verbose_name= '密码')
    is_manager = models.BooleanField(default=False, verbose_name='是否是管理员')
    sex = models.CharField(choices=SEX_CHOICES,max_length=4,verbose_name='性别')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户表'

class Computer(models.Model):
    computername = models.CharField(max_length=100,verbose_name='主机名')
    memory = models.CharField(max_length=100,verbose_name='内存')

    state = models.BooleanField(verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User,related_name='user_computer')

    def __str__(self):
        return  self.computername
    class Meta:
        verbose_name = '主机'
        verbose_name_plural = '主机表'