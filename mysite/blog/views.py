#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
def index(req):
    return render_to_response("index.html")

def login(req):
    return render_to_response("login.html")

def register(req):
    return render_to_response("register.html")

def management_user(req):
    return render_to_response("management_user.html")

def management_computer(req):
    return render_to_response("management_computer.html")

def account_setting(req):
    return render_to_response("account_setting.html")

def index(req):
    username = req.COOKIES.get('username',"")
    computers = Computer.objects.all()
    return render_to_response("index.html",{"computers":computers,'username':username})

def acc_regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    print username,password,repassword
    return render_to_response("index.html")
    if users.objects.all().filter(username = username):
        return render_to_response("用户已存在")
    else:
        if password == repassword:
            User.object.create(username = username,password = password)
            username = request.COOKIES.get('username',"")
            computers = Computer.objects.all()
            return render_to_response("index.html",{"blogs":blogs,'username':username})
        else:
            return render_to_response("注册成功")

def acc_login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    if User.objects.all().filter(username=username):
        user = User.objects.all().get(username=username)
        if password == password:
            response = HttpResponseRedirect('/')
            response.set_cookie('username',username,3600)
            return response
        else:
            return render_to_response("login.html",{'error':'成功'})
    else:
        return render_to_response("login.html",{'error':'去死吧'})

def logout(req):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response