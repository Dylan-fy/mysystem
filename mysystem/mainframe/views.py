# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
import os
from models import Computer
from django.template import RequestContext
from mainframe.models import User
from django import forms
from .models import *
# Create your views here.

def home(req):
    return render_to_response("home.html")

def login(req):
    return render_to_response("login.html")

def registration(req):
    return render_to_response("registration.html")

def cp_update(req):
    return render_to_response("cp_update.html")

def host_management(request):
    username = request.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    computer = Computer.objects.filter(user=user)
    # state = Computer.objects.get(computer).state
    # if state:
    #     Computer.objects.filter(computer=computer).update(state=True)
    # else:
    #     Computer.objects.filter(computer=computer).update(state=False)
    return render(request,'host_management.html',{'computer':computer})

def user_management(request):
    username = request.COOKIES.get('username', '')
    user = User.objects.filter(username = username)
    return render(request, 'user_management.html', {'user': user})

def update_computer(request,computer_id):
    state = Computer.objects.get(id = computer_id).state
    if state:
        Computer.objects.filter(id = computer_id).update(state=True)
    else:
        Computer.objects.filter(id = computer_id).update(state=False)
    return render(request,'host_management.html',{'computer_id':computer_id})

def personal_center(req):
    return render_to_response("personal_center.html")
def add(req):
    return render_to_response("add.html")

def success(req):
    return render_to_response("success.html")

def new(req):
    return render_to_response("new.html")

def mainframe_one(req):
    return render_to_response("mainframe_one.html")

def index(req):
    username=req.COOKIES.get('username',"")
    computers = Computer.objects.all()
    return render_to_response("home.html",{"computers":computers, 'username':username})

def acc_regist(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    print username, password, repassword

    if User.objects.all().filter(username = username):
        return render_to_response("registration.html", {'error': '用户名已存在！'})
    else:
        if password == repassword:
            User.objects.create(username = username,password = password)
            username = request.COOKIES.get('username', "")
            computers = Computer.objects.all()
            return render_to_response("login.html", {'error':'注册成功！'})
        else:
            return render_to_response("registration.html", {'error': '两次输入的密码不一致！'})



def acc_login(requset):
    username = requset.POST.get('username')
    password = requset.POST.get('password')
    if User.objects.all().filter(username=username):
        user= User.objects.all().get(username=username)
        if password==user.password:
            response = HttpResponseRedirect('/home/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return render_to_response('login.html', {'error': '密码错误！'})

    else:
        return render_to_response("login.html", {'error': '用户不存在！'})

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response

def chakan(request):
    vm_num = os.popen('VBoxManage list vms')
    return HttpResponse('查看当前虚拟机有{}'.format(vm_num))
#
def close_user_Computer(request):
    os.system('关掉xx的用户的虚拟机')
    Computer.state = '已关机'
    return  HttpResponse('xx的计算机已关闭')

def kelong(request):
    # os.popen(r'C:\Program Files\Oracle\VirtualBox>"C:\Users\Dylan\VirtualBox VMs\2\2.vdi" "C:\Users\Dylan\VirtualBox VMs\2\4.vdi"')
    os.system(r'''C:\Program\000Files\Oracle\VirtualBox>vboxmanage.exe\000clonevdi\000"C:\Users\Dylan\VirtualBox\000VMs\2\2.vdi" "C:\Users\Dylan\VirtualBox\000VMs\2\4.vdi"''')
    return HttpResponse('xx')
    # print output
    # return HttpResponse(output)

def create_cp(request):
    cpname = request.GET.get('cpname')
    cpuser = request.GET.get('cpuser')
    memory = request.POST.get('password')
    repassword = request.POST.get('repassword')

def user_delete(request,user_id):
    User.objects.filter(id=user_id).delete()
    return HttpResponse("删除成功！")

def cp_delete(request,cp_id):
    Computer.objects.filter(id=cp_id).delete()
    return HttpResponse("删除成功！")

def user_list(req):
    return render_to_response("user_list.html")

def user_ls(request,user_id):
    user_l = User.objects.all().get(id=user_id)
    return render(request, 'user_list.html', {'user_l': user_l})

# def computer(request):
#     username = request.COOKIES.get('username','')
#     if username:
#         user = Computer.objects.all().get(user = username)
#         return  render(request,"host_management.html",{'Computer':user})
#     else:
#         return render_to_response("login.html",{'error':'请先登录！'})












