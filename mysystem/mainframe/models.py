# coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    # SEX_CHOICES =(
    #     (u'男',u'男'),
    #     (u'女',u'女'),
    # )
    username = models.CharField(max_length=100, verbose_name= '用户名')
    password = models.CharField(max_length=200,verbose_name= '密码')
    # sex = models.CharField(choices=SEX_CHOICES,max_length=4,verbose_name='性别')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户表'

class Computer(models.Model):
    computername = models.CharField(max_length=100,verbose_name='主机名')
    user = models.ForeignKey(User, related_name='user_computer', verbose_name='用户')
    config = models.TextField(verbose_name='主机配置', blank=True, null=True)
    ip_address = models.CharField(
        max_length=50, default='0.0.0.0', verbose_name='主机ip地址')
    password = models.CharField(
        max_length=100, default='123456', verbose_name='主机登录密码')
    username = models.CharField(
        max_length=100, default='root', verbose_name='主机登录用户名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return  self.computername
    class Meta:
        verbose_name = '主机'
        verbose_name_plural = '主机表'