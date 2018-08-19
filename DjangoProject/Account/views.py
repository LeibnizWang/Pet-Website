# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Pet.models import sort
import smtplib,email
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
ctx={}

def contact(request):
    return render(request, "contact-form-2.html",ctx)

def create_account(request):
    return render(request, "create-account.html",ctx)

def payment_form(request):
    return render(request, "payment-form.html",ctx)

def forgot_password(request):
    return render(request, "forgot-password.html",ctx)

def help(request):
    result={}
    if request.user.is_authenticated():
        result['link']='/Pet/forum-search?keywords='+request.user.username
        return render(request, "help.html",result)
    else:
        return redirect("/Account/login-2")
#旧版登陆界面
def login_1(request):
    return render(request, "login-1.html",ctx)
#新版登录界面
def login_2(request):
    return render(request, "login-2.html",ctx)

#修改密码
def change_submit(request):
    if request.user.is_authenticated():
        #
        user=User.objects.get(username=request.user.username)
        if request.GET['new_password']==request.GET['comfirm_new_password']:
            user.set_password(request.GET['new_password'])
            logout(request)
            user.save()
            return HttpResponse("<script>  alert(\"密码修改成功,请重新登录!\"); window.location.href=\"/Account/login-2\" </script>")
        else:
            return HttpResponse("<script>  alert(\"请输入相同的密码!\"); </script>")
    else:
        return redirect("/Account/login-2")
    
#注册函数
def create_account_submit(request):
    request.encoding='utf-8'
    Errorflag=0
    create_account_message={}
    if 'first_name' in request.GET:
        create_account_message['first_name_message']=' '
    else:
        create_account_message['first_name_message']='请输入名字'
        Errorflag=1

    if 'last_name' in request.GET:
        #create_account_message['last_name_message']=' '
        pass
    else:
        create_account_message['last_name_message']='请输入姓'
        Errorflag=1

    if 'email' in request.GET:
        #create_account_message['email_message']=' '
        pass
    else:
        create_account_message['email_message']='请输入邮箱'
        Errorflag=1

    if 'username' in request.GET:
        try:
            response = User.objects.get(username=request.GET['username'])
            create_account_message['username_message']='该用户名已被注册'
            Errorflag=1
        except:
            pass
    else:
        create_account_message['username_message']='请输入用户名'
        Errorflag=1

    if 'password' in request.GET:
        #create_account_message['password_message']=' '
        pass
    else:
        create_account_message['password_message']='请输入密码'
        Errorflag=1

    if 'password_confirm' in request.GET:
        if request.GET['password_confirm']==request.GET['password']:
            pass
        else:
           create_account_message['password_confirm_message']='请输入相同的密码' 
           Errorflag=1
    else:
        create_account_message['password_confirm_message']='请再次输入密码'
        Errorflag=1
    
    if Errorflag==1:
        create_account_message['result_message']='请检查信息'
        return render(request, "create-account.html",create_account_message) 
    else:
        user=User.objects.create_user(username=request.GET['username'],
            email=request.GET['email'],
            password=request.GET['password'],
            first_name=request.GET['first_name'],
            last_name=request.GET['last_name'])
        user.save()
        #生成检索排序表单
        user1=sort()
        user1.username=user.username
        user1.save()

        create_account_message['result_message']='注册成功'
        return HttpResponse("<script>  alert(\"注册成功!\"); window.location.href=\"/Account/login-2\" </script>")
        #return render(request, "create-account.html",create_account_message)
        #return redirect("/Account/login-1")

#登录函数
def login_submit(request):
    request.encoding='utf-8'
    login_message={}
    username=request.GET['username']
    password=request.GET['password']

    user=authenticate(username=username,password=password)

    if user:
        login(request,user)
        #return redirect("/")
        return HttpResponse("<script>  alert(\"登录成功!\"); window.location.href=\"/\" </script>")

    else:
        login_message['message']='用户名或密码错误'
        return render(request,"login-1.html",login_message)

def login_submit_new(request):
    request.encoding='utf-8'
    login_message={}
    username=request.GET['username']
    password=request.GET['password']

    user=authenticate(username=username,password=password)

    if user:
        login(request,user)
        #return redirect("/")
        return HttpResponse("<script>  alert(\"登录成功!\"); window.location.href=\"/\" </script>")

    else:
        login_message['message']='用户名或密码错误'
        return render(request,"login-2.html",login_message)

def contact_submit(request):
    request.encoding='utf-8'
    #contact_message={}
    subject=request.GET['subject']
    name=request.GET['name']
    email=request.GET['email']
    phone=request.GET['phone']
    message=request.GET['message']

    #chst=email.charset.Charset(input_charset='utf-8')
    header=("From: %s\nTo: %s\nSubject: %s\n\n"
            %("leibnizwang@163.com",
            "leibnizwang@163.com",
            "Bug反馈!"))       #邮件标题内容
    body="主题："+subject+"\n"                     #邮件主题内容
    body=body+"姓名："+name+"\n"
    body=body+"邮箱地址："+email+"\n"
    body=body+"电话号码："+phone+"\n"
    body=body+"内容："+message+"\n"
    email_con=header.encode('utf-8')+body.encode('utf-8')
    smtp=smtplib.SMTP("smtp.163.com")
    smtp.login("leibnizwang@163.com","Wzh970818")
    smtp.sendmail("leibnizwang@163.com","leibnizwang@163.com",email_con)
    smtp.quit()
    #contact_message['message']="反馈成功"
    #return render(request,"contact-form-2.html",contact_message)
    return HttpResponse("<script>  alert(\"反馈成功!\"); window.location.href=\"/\" </script>")

def userlogout(request):
    logout(request)
    return HttpResponse("<script>  alert(\"登出成功!\"); window.location.href=\"/\" </script>")