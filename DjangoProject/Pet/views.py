# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response,HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Pet.models import Guy,sort,Deal,Card
from PIL import Image
from Pet.tests import op
import smtplib,email
import os,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
ctx={}

def contact(request):
    return render(request, "contact.html",ctx)

def center(request):
    return render(request, "center.html",ctx)

def adoption(request):
    return render(request, "adoption.html",ctx)

def fostering(request):
    return render(request, "fostering.html",ctx)

def index(request):
    if request.user.is_authenticated():
        ctx['welcome']='欢迎,'+request.user.username
    else:
        ctx['welcome']='欢迎光临宠物寄养信息平台！'
    return render(request, "index.html",ctx)

def match(request):
    return render(request, "match.html",ctx)

def adoption_submit(request):
    if request.method=='POST':
        #name=request.COOKIES.get('username')
        #name=True
        if request.user.is_authenticated():
            try:
                user=Guy.objects.get(username=request.user.username)
                user.phone=request.POST.get('phone')
                user.address=request.POST.get('address')
                user.experience=request.POST.get('experience')
                user.seed=request.POST.get('seed')
                user.price=request.POST.get('price')
                user.information=request.POST.get('information')
                user.animal_info=request.POST.get('animal_info')
                try:
                    image=request.FILES.get('images')
                    #image.name=str(username)+'.jpg'
                    if image.size>10000 and image.size<20480000:
                        path=default_storage.save('Pet/static/images/UserhomeImages/'+image.name,ContentFile(image.read()))
                        #tmp_file=os.path.join(settings.BASE_DIR,path)
                        user.picture='/static/images/UserhomeImages/'+image.name
                    else:
                        #return HttpResponse("<p>图片应在2M之内！</p>")
                        return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
                except:
                    #return HttpResponse("<p>Error!</p>")
                    return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
                    
                user.save()
                #im = Image.open(user.picture)
                #image_resized = im.resize((480,280), Image.ANTIALIAS)
                #image_resized.save(user.picture, 'jpeg')
                return HttpResponse("<script>  alert(\"用户信息更新成功!\"); window.location.href=\"/Pet/adoption\" </script>")
            except:
                user=Guy()
                user.username=request.user.username
                user.phone=request.POST.get('phone')
                user.address=request.POST.get('address')
                user.experience=request.POST.get('experience')
                user.seed=request.POST.get('seed')
                user.price=request.POST.get('price')
                user.information=request.POST.get('information')
                user.animal_info=request.POST.get('animal_info')
                try:
                    image=request.FILES.get('images')
                    #image.name=str(username)+'.jpg'
                    if image.size>10000 and image.size<20480000:
                        path=default_storage.save('Pet/static/images/UserhomeImages/'+image.name,ContentFile(image.read()))
                        #tmp_file=os.path.join(settings.BASE_DIR,path)
                        user.picture='/static/images/UserhomeImages/'+image.name
                    else:
                        #return HttpResponse("<p>图片应在2M之内！</p>")
                        return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
                except:
                    #return HttpResponse("<p>Error!</p>")
                    return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")   
                user.save()
                #im = Image.open(user.picture)
                #image_resized = im.resize((480,280), Image.ANTIALIAS)
                #image_resized.save(user.picture, 'jpeg')
                return HttpResponse("<script>  alert(\"申请成功!\"); window.location.href=\"/Pet/adoption\" </script>")
        else:
            return redirect("/Account/login-2")

def contact_submit(request):
    request.encoding='utf-8'
    #contact_message={}
    name=request.GET['name']
    email=request.GET['email']
    phone=request.GET['phone']
    message=request.GET['message']

    #chst=email.charset.Charset(input_charset='utf-8')
    header=("From: %s\nTo: %s\nSubject: %s\n\n"
            %("leibnizwang@163.com",
            "leibnizwang@163.com",
            "Bug反馈!"))       #邮件标题内容 
    body="姓名："+name+"\n"
    body=body+"邮箱地址："+email+"\n"
    body=body+"电话号码："+phone+"\n"
    body=body+"内容："+message+"\n"
    email_con=header.encode('utf-8')+body.encode('utf-8')
    smtp=smtplib.SMTP("smtp.163.com")
    smtp.login("leibnizwang@163.com","Wzh970818")
    smtp.sendmail("leibnizwang@163.com","leibnizwang@163.com",email_con)
    smtp.quit()
    #contact_message['message']="反馈成功"
    return HttpResponse("<script>  alert(\"反馈成功!\"); window.location.href=\"/\" </script>")
    #return render(request,"contact.html",contact_message)

def fostering_submit(request):
    if request.user.is_authenticated():
        result={}
        #result['result1_picture']='/static/images/e1.jpg'
        #result['result2_picture']='/static/images/e2.jpg'
        #result['result3_picture']='/static/images/e3.jpg'
        #result['result4_picture']='/static/images/e4.jpg'
        #result['result5_picture']='/static/images/e5.jpg'
        #result['result6_picture']='/static/images/e6.jpg'
        #result['result7_picture']='/static/images/e7.jpg'
        #result['result8_picture']='/static/images/e8.jpg'
        cityget=request.GET['city']
        seedget=request.GET['seed']
        option=request.GET['optionsRadios']
        if(option=='option1'):
            resultlist=Guy.objects.filter(city=cityget,seed=seedget).order_by("score")
            resultname0=''
            for result0 in resultlist:
                resultname0=resultname0+result0.username+'-'
            sort1=sort.objects.get(username=request.user.username)
            sort1.flag=0
            sort1.resultname=resultname0
            sort1.result1=resultlist[0].username
            sort1.result2=resultlist[1].username
            sort1.result3=resultlist[2].username
            sort1.result4=resultlist[3].username
            sort1.result5=resultlist[4].username
            sort1.result6=resultlist[5].username
            sort1.result7=resultlist[6].username
            sort1.result8=resultlist[7].username
            sort1.save()
            result['result1_username']=resultlist[0].username
            result['result1_address']=resultlist[0].address
            result['result1_information']=resultlist[0].information
            result['result1_experience']=resultlist[0].experience
            result['result1_price']=resultlist[0].price
            result['result1_picture']=resultlist[0].picture
            result['result2_username']=resultlist[1].username
            result['result2_address']=resultlist[1].address
            result['result2_information']=resultlist[1].information
            result['result2_experience']=resultlist[1].experience
            result['result2_price']=resultlist[1].price
            result['result2_picture']=resultlist[1].picture
            result['result3_username']=resultlist[2].username
            result['result3_address']=resultlist[2].address
            result['result3_information']=resultlist[2].information
            result['result3_experience']=resultlist[2].experience
            result['result3_price']=resultlist[2].price
            result['result3_picture']=resultlist[2].picture
            result['result4_username']=resultlist[3].username
            result['result4_address']=resultlist[3].address
            result['result4_information']=resultlist[3].information
            result['result4_experience']=resultlist[3].experience
            result['result4_price']=resultlist[3].price
            result['result4_picture']=resultlist[3].picture
            result['result5_username']=resultlist[4].username
            result['result5_address']=resultlist[4].address
            result['result5_information']=resultlist[4].information
            result['result5_experience']=resultlist[4].experience
            result['result5_price']=resultlist[4].price
            result['result5_picture']=resultlist[4].picture
            result['result6_username']=resultlist[5].username
            result['result6_address']=resultlist[5].address
            result['result6_information']=resultlist[5].information
            result['result6_experience']=resultlist[5].experience
            result['result6_price']=resultlist[5].price
            result['result6_picture']=resultlist[5].picture
            result['result7_username']=resultlist[6].username
            result['result7_address']=resultlist[6].address
            result['result7_information']=resultlist[6].information
            result['result7_experience']=resultlist[6].experience
            result['result7_price']=resultlist[6].price
            result['result7_picture']=resultlist[6].picture
            result['result8_username']=resultlist[7].username
            result['result8_address']=resultlist[7].address
            result['result8_information']=resultlist[7].information
            result['result8_experience']=resultlist[7].experience
            result['result8_price']=resultlist[7].price
            result['result8_picture']=resultlist[7].picture
        if(option=='option2'):
            resultlist=Guy.objects.filter(city=cityget,seed=seedget).order_by("price")
            resultname0=''
            for result0 in resultlist:
                resultname0=resultname0+result0.username+'-'
            sort1=sort.objects.get(username=request.user.username)
            sort1.flag=0
            sort1.resultname=resultname0
            sort1.result1=resultlist[0].username
            sort1.result2=resultlist[1].username
            sort1.result3=resultlist[2].username
            sort1.result4=resultlist[3].username
            sort1.result5=resultlist[4].username
            sort1.result6=resultlist[5].username
            sort1.result7=resultlist[6].username
            sort1.result8=resultlist[7].username
            sort1.save()
            result['result1_username']=resultlist[0].username
            result['result1_address']=resultlist[0].address
            result['result1_information']=resultlist[0].information
            result['result1_experience']=resultlist[0].experience
            result['result1_price']=resultlist[0].price
            result['result1_picture']=resultlist[0].picture
            result['result2_username']=resultlist[1].username
            result['result2_address']=resultlist[1].address
            result['result2_information']=resultlist[1].information
            result['result2_experience']=resultlist[1].experience
            result['result2_price']=resultlist[1].price
            result['result2_picture']=resultlist[1].picture
            result['result3_username']=resultlist[2].username
            result['result3_address']=resultlist[2].address
            result['result3_information']=resultlist[2].information
            result['result3_experience']=resultlist[2].experience
            result['result3_price']=resultlist[2].price
            result['result3_picture']=resultlist[2].picture
            result['result4_username']=resultlist[3].username
            result['result4_address']=resultlist[3].address
            result['result4_information']=resultlist[3].information
            result['result4_experience']=resultlist[3].experience
            result['result4_price']=resultlist[3].price
            result['result4_picture']=resultlist[3].picture
            result['result5_username']=resultlist[4].username
            result['result5_address']=resultlist[4].address
            result['result5_information']=resultlist[4].information
            result['result5_experience']=resultlist[4].experience
            result['result5_price']=resultlist[4].price
            result['result5_picture']=resultlist[4].picture
            result['result6_username']=resultlist[5].username
            result['result6_address']=resultlist[5].address
            result['result6_information']=resultlist[5].information
            result['result6_experience']=resultlist[5].experience
            result['result6_price']=resultlist[5].price
            result['result6_picture']=resultlist[5].picture
            result['result7_username']=resultlist[6].username
            result['result7_address']=resultlist[6].address
            result['result7_information']=resultlist[6].information
            result['result7_experience']=resultlist[6].experience
            result['result7_price']=resultlist[6].price
            result['result7_picture']=resultlist[6].picture
            result['result8_username']=resultlist[7].username
            result['result8_address']=resultlist[7].address
            result['result8_information']=resultlist[7].information
            result['result8_experience']=resultlist[7].experience
            result['result8_price']=resultlist[7].price
            result['result8_picture']=resultlist[7].picture

        if(option=='option3'):
            resultlist=Guy.objects.filter(city=cityget,seed=seedget).order_by("experience")
            resultname0=''
            for result0 in resultlist:
                resultname0=resultname0+result0.username+'-'
            sort1=sort.objects.get(username=request.user.username)
            sort1.flag=0
            sort1.resultname=resultname0
            sort1.result1=resultlist[0].username
            sort1.result2=resultlist[1].username
            sort1.result3=resultlist[2].username
            sort1.result4=resultlist[3].username
            sort1.result5=resultlist[4].username
            sort1.result6=resultlist[5].username
            sort1.result7=resultlist[6].username
            sort1.result8=resultlist[7].username
            sort1.save()
            result['result1_username']=resultlist[0].username
            result['result1_address']=resultlist[0].address
            result['result1_information']=resultlist[0].information
            result['result1_experience']=resultlist[0].experience
            result['result1_price']=resultlist[0].price
            result['result1_picture']=resultlist[0].picture
            result['result2_username']=resultlist[1].username
            result['result2_address']=resultlist[1].address
            result['result2_information']=resultlist[1].information
            result['result2_experience']=resultlist[1].experience
            result['result2_price']=resultlist[1].price
            result['result2_picture']=resultlist[1].picture
            result['result3_username']=resultlist[2].username
            result['result3_address']=resultlist[2].address
            result['result3_information']=resultlist[2].information
            result['result3_experience']=resultlist[2].experience
            result['result3_price']=resultlist[2].price
            result['result3_picture']=resultlist[2].picture
            result['result4_username']=resultlist[3].username
            result['result4_address']=resultlist[3].address
            result['result4_information']=resultlist[3].information
            result['result4_experience']=resultlist[3].experience
            result['result4_price']=resultlist[3].price
            result['result4_picture']=resultlist[3].picture
            result['result5_username']=resultlist[4].username
            result['result5_address']=resultlist[4].address
            result['result5_information']=resultlist[4].information
            result['result5_experience']=resultlist[4].experience
            result['result5_price']=resultlist[4].price
            result['result5_picture']=resultlist[4].picture
            result['result6_username']=resultlist[5].username
            result['result6_address']=resultlist[5].address
            result['result6_information']=resultlist[5].information
            result['result6_experience']=resultlist[5].experience
            result['result6_price']=resultlist[5].price
            result['result6_picture']=resultlist[5].picture
            result['result7_username']=resultlist[6].username
            result['result7_address']=resultlist[6].address
            result['result7_information']=resultlist[6].information
            result['result7_experience']=resultlist[6].experience
            result['result7_price']=resultlist[6].price
            result['result7_picture']=resultlist[6].picture
            result['result8_username']=resultlist[7].username
            result['result8_address']=resultlist[7].address
            result['result8_information']=resultlist[7].information
            result['result8_experience']=resultlist[7].experience
            result['result8_price']=resultlist[7].price
            result['result8_picture']=resultlist[7].picture
        #result['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return render(request, "match.html",result)
    else:
        return HttpResponse("<script>  alert(\"您尚未登录。\"); window.location.href=\"/Account/login-2\" </script>")

def refresh(request):
    result={}
    #result['result1_picture']='/static/images/e1.jpg'
    #result['result2_picture']='/static/images/e2.jpg'
    #result['result3_picture']='/static/images/e3.jpg'
    #result['result4_picture']='/static/images/e4.jpg'
    #result['result5_picture']='/static/images/e5.jpg'
    #result['result6_picture']='/static/images/e6.jpg'
    #result['result7_picture']='/static/images/e7.jpg'
    #result['result8_picture']='/static/images/e8.jpg'
    sort1=sort.objects.get(username=request.user.username)
    resultlist=sort1.resultname.split("-")
    length=len(resultlist)
    sort1.flag+=1
    sort1.result1=resultlist[(sort1.flag*8+0)%(length-1)]
    sort1.result2=resultlist[(sort1.flag*8+1)%(length-1)]
    sort1.result3=resultlist[(sort1.flag*8+2)%(length-1)]
    sort1.result4=resultlist[(sort1.flag*8+3)%(length-1)]
    sort1.result5=resultlist[(sort1.flag*8+4)%(length-1)]
    sort1.result6=resultlist[(sort1.flag*8+5)%(length-1)]
    sort1.result7=resultlist[(sort1.flag*8+6)%(length-1)]
    sort1.result8=resultlist[(sort1.flag*8+7)%(length-1)]
    sort1.save()
    result['result1_username']=Guy.objects.get(username=sort1.result1).username
    result['result1_address']=Guy.objects.get(username=sort1.result1).address
    result['result1_information']=Guy.objects.get(username=sort1.result1).information
    result['result1_experience']=Guy.objects.get(username=sort1.result1).experience
    result['result1_price']=Guy.objects.get(username=sort1.result1).price
    result['result1_picture']=Guy.objects.get(username=sort1.result1).picture
    result['result2_username']=Guy.objects.get(username=sort1.result2).username
    result['result2_address']=Guy.objects.get(username=sort1.result2).address
    result['result2_information']=Guy.objects.get(username=sort1.result2).information
    result['result2_experience']=Guy.objects.get(username=sort1.result2).experience
    result['result2_price']=Guy.objects.get(username=sort1.result2).price
    result['result2_picture']=Guy.objects.get(username=sort1.result2).picture
    result['result3_username']=Guy.objects.get(username=sort1.result3).username
    result['result3_address']=Guy.objects.get(username=sort1.result3).address
    result['result3_information']=Guy.objects.get(username=sort1.result3).information
    result['result3_experience']=Guy.objects.get(username=sort1.result3).experience
    result['result3_price']=Guy.objects.get(username=sort1.result3).price
    result['result3_picture']=Guy.objects.get(username=sort1.result3).picture
    result['result4_username']=Guy.objects.get(username=sort1.result4).username
    result['result4_address']=Guy.objects.get(username=sort1.result4).address
    result['result4_information']=Guy.objects.get(username=sort1.result4).information
    result['result4_experience']=Guy.objects.get(username=sort1.result4).experience
    result['result4_price']=Guy.objects.get(username=sort1.result4).price
    result['result4_picture']=Guy.objects.get(username=sort1.result4).picture
    result['result5_username']=Guy.objects.get(username=sort1.result5).username
    result['result5_address']=Guy.objects.get(username=sort1.result5).address
    result['result5_information']=Guy.objects.get(username=sort1.result5).information
    result['result5_experience']=Guy.objects.get(username=sort1.result5).experience
    result['result5_price']=Guy.objects.get(username=sort1.result5).price
    result['result5_picture']=Guy.objects.get(username=sort1.result5).picture
    result['result6_username']=Guy.objects.get(username=sort1.result6).username
    result['result6_address']=Guy.objects.get(username=sort1.result6).address
    result['result6_information']=Guy.objects.get(username=sort1.result6).information
    result['result6_experience']=Guy.objects.get(username=sort1.result6).experience
    result['result6_price']=Guy.objects.get(username=sort1.result6).price
    result['result6_picture']=Guy.objects.get(username=sort1.result6).picture
    result['result7_username']=Guy.objects.get(username=sort1.result7).username
    result['result7_address']=Guy.objects.get(username=sort1.result7).address
    result['result7_information']=Guy.objects.get(username=sort1.result7).information
    result['result7_experience']=Guy.objects.get(username=sort1.result7).experience
    result['result7_price']=Guy.objects.get(username=sort1.result7).price
    result['result7_picture']=Guy.objects.get(username=sort1.result7).picture
    result['result8_username']=Guy.objects.get(username=sort1.result8).username
    result['result8_address']=Guy.objects.get(username=sort1.result8).address
    result['result8_information']=Guy.objects.get(username=sort1.result8).information
    result['result8_experience']=Guy.objects.get(username=sort1.result8).experience
    result['result8_price']=Guy.objects.get(username=sort1.result8).price
    result['result8_picture']=Guy.objects.get(username=sort1.result8).picture
    #result['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return render(request, "match.html",result)


def makesure1_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result1
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure2_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result2
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure3_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result3
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure4_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result4
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure5_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result5
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure6_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result6
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure7_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result7
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure8_submit(request):
    deal=Deal()
    deal.askname=request.user.username
    deal.receivename=sort.objects.get(username=request.user.username).result8
    deal.seed=request.POST.get('seed')
    deal.price=request.POST.get('price')
    deal.time=request.POST.get('time')
    deal.information=request.POST.get('information')
    deal.state="待确认"
    try:
        image=request.FILES.get('images')
        #image.name=str(username)+'.jpg'
        if image.size>10000 and image.size<20480000:
            path=default_storage.save('Pet/static/images/UserpetImages/'+image.name,ContentFile(image.read()))
            #tmp_file=os.path.join(settings.BASE_DIR,path)
            deal.picture='/static/images/UserpetImages/'+image.name
        else:
            #return HttpResponse("<p>图片应在2M之内！</p>")
            return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/adoption\" </script>")
    except:
        #return HttpResponse("<p>Error!</p>")
        return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/adoption\" </script>")
    deal.save()
    #return render(request,"index.html",ctx)
    return HttpResponse("<script>  alert(\"下单成功!请及时注意状态更新！\"); window.location.href=\"/Pet/index\" </script>")

def makesure1(request):
    return render(request,"makesure1.html",ctx)

def makesure2(request):
    return render(request,"makesure2.html",ctx)

def makesure3(request):
    return render(request,"makesure3.html",ctx)

def makesure4(request):
    return render(request,"makesure4.html",ctx)

def makesure5(request):
    return render(request,"makesure5.html",ctx)

def makesure6(request):
    return render(request,"makesure6.html",ctx)

def makesure7(request):
    return render(request,"makesure7.html",ctx)

def makesure8(request):
    return render(request,"makesure8.html",ctx)

def personal(request):
    if request.user.is_authenticated():
        result={}
        try:
            deal1=Deal.objects.filter(receivename=request.user.username,state="待确认").order_by("id")[0]
            result['receive_picture']=deal1.picture
            result['receive_seed']=deal1.seed
            result['receive_price']=deal1.price
            result['receive_time']=deal1.time
            result['receive_information']=deal1.information
        
        except:
            result['receive_picture']='/static/images/e1.jpg'
            result['receive_seed']='无'
            result['receive_price']='无'
            result['receive_time']='无'
            result['receive_information']='无'
        

        try:
            deal2=Deal.objects.filter(askname=request.user.username).exclude(state='已完成').order_by("id")[0]
            result['ask_picture']=deal2.picture
            result['ask_seed']=deal2.seed
            result['ask_price']=deal2.price
            result['ask_time']=deal2.time
            result['ask_state']=deal2.state
        except:
            result['ask_picture']='/static/images/e1.jpg'
            result['ask_seed']="无"
            result['ask_price']="无"
            result['ask_time']="无"
            result['ask_state']="无"

        try:
            deal3=Deal.objects.filter(askname=request.user.username,state='已完成').order_by("-id")[0]
            result['done_picture']=deal3.picture
            result['done_seed']=deal3.seed
            result['done_price']=deal3.price
            result['done_time']=deal3.time
            #result['ask_state']=deal3.state
        except:
            try:
                deal4=Deal.objects.filter(receivename=request.user.username,state='已完成').order_by("-id")[0]
                result['done_picture']=deal4.picture
                result['done_seed']=deal4.seed
                result['done_price']=deal4.price
                result['done_time']=deal4.time
            except:
                result['done_picture']='/static/images/e1.jpg'
                result['done_seed']="无"
                result['done_price']="无"
                result['done_time']="无"
        return render(request,"personal.html",result)
    else:
        return redirect("/Account/login-2")

def agree(request):
    try:
        deal1=Deal.objects.filter(receivename=request.user.username,state='待确认')[0]
        deal1.state='已确认'
        deal1.save()
        try:
            #给寄养方发送邮件
            person1=User.objects.get(username=deal1.askname)
            person2=User.objects.get(username=deal1.receivename)
            person2info=Guy.objects.get(username=deal1.receivename)
            #chst=email.charset.Charset(input_charset='utf-8')
            header1=("From: %s\nTo: %s\nSubject: %s\n\n"
                    %("leibnizwang@163.com",
                    person1.email,
                    "bitpet提醒，您的宠物寄养请求已经通过！"))       #邮件标题内容 
            body1="亲爱的用户您好 ^_^ ，您的宠物寄养请求已经通过！\n温馨提示：bitpet感谢您对bitpet宠物寄养平台的信任，预祝一切顺利 ^_^ \n"
            body1="收养方姓名："+person2.username+"\n"
            body1=body1+"邮箱地址："+person2.email+"\n"
            body1=body1+"电话号码："+person2info.phone+"\n"
            body1=body1+"详细地址："+person2info.address+"\n"
            body1=body1+"内容：以上为您选择的收养方的详细信息，请您自行与其联系，祝好！\n"
            body1=body1+"bitpet提示：请不要利用对方个人信息进行违规操作包括但不限于贩卖私人信息、利用信息对私人进行骚扰等。如有意外发生，本平台概不负责。\n"
            body1=body1+"bitpet网站是 http://www.bitpet.xyz"
            body1=body1+"客服QQ是 596928069"
            body1=body1+"客服微信是 suxiaocantangxiaowu"
            body1=body1+"客服电话是 18810583628"
            body1=body1+"客服邮箱是 596928069@qq.com"
            body1=body1+"bitpet，千万萌宠主人的选择，再次感谢您选择bitpet宠物寄养平台 ^_^"
            body1=body1+"收养宠物，找bitpet！寄养宠物，找bitpet！"
            email_con1=header1.encode('utf-8')+body1.encode('utf-8')
            #给收养方发送邮件
            header2=("From: %s\nTo: %s\nSubject: %s\n\n"
                    %("leibnizwang@163.com",
                    person2.email,
                    "请求反馈!"))       #邮件标题内容 
            body2="寄养方姓名："+person1.username+"\n"
            body2=body2+"邮箱地址："+person1.email+"\n"
            body2=body2+"内容：这是您选择的收养方的基本信息，希望合作愉快！\n"
            body2=body2+"bitpet提示：请不要利用对方个人信息进行违规操作包括但不限于贩卖私人信息、利用信息对私人进行骚扰等。如有意外发生，本平台概不负责。\n"
            body2=body2+"bitpet网站是 http://www.bitpet.xyz\n"
            body2=body2+"客服QQ是 596928069"
            body2=body2+"客服微信是 suxiaocantangxiaowu"
            body2=body2+"客服电话是 18810583628"
            body2=body2+"客服邮箱是 596928069@qq.com"
            body2=body2+"bitpet，千万萌宠主人的选择，再次感谢您选择bitpet宠物寄养平台 ^_^\n"
            body2=body2+"收养宠物，找bitpet！寄养宠物，找bitpet！\n"
            email_con2=header2.encode('utf-8')+body2.encode('utf-8')

            smtp=smtplib.SMTP("smtp.163.com")
            smtp.login("leibnizwang@163.com","Wzh970818")
            smtp.sendmail("leibnizwang@163.com",person1.email,email_con1)
            smtp.sendmail("leibnizwang@163.com",person2.email,email_con2)
            smtp.quit()
        except:
            return HttpResponse("<script>  alert(\"发生了一些未知的错误，我们将尽快为您解决，如果您有特殊情况，请和我们联系。\"); window.location.href=\"/Pet/personal\" </script>")
        return HttpResponse("<script>  alert(\"您接受了该订单，我们已将用户信息发送至您的邮箱。\"); window.location.href=\"/Pet/personal\" </script>")
    except:
        return HttpResponse("<script>  alert(\"您没有未处理的订单。\"); window.location.href=\"/Pet/personal\" </script>") 

def refuse(request):
    try:
        deal1=Deal.objects.filter(receivename=request.user.username,state='待确认')[0]
        deal1.state='对不起，您的请求被拒绝。'
        deal1.save()
        return HttpResponse("<script>  alert(\"您拒绝了该订单。\"); window.location.href=\"/Pet/personal\" </script>") 
    except:
        return HttpResponse("<script>  alert(\"您没有未处理的订单。\"); window.location.href=\"/Pet/personal\" </script>") 

def done(request):
    try:
        deal1=Deal.objects.filter(askname=request.user.username).exclude(state='已完成')[0]
        deal1.state='已完成'
        deal1.save()
        return HttpResponse("<script>  alert(\"您的订单已完成。\"); window.location.href=\"/Pet/personal\" </script>")
    except:
        return HttpResponse("<script>  alert(\"您无法结束该订单。\"); window.location.href=\"/Pet/personal\" </script>")

def poster(request):
    return render(request,"post.html",ctx)

def poster_submit(request):
    if request.user.is_authenticated():
        card=Card()
        card.postname=request.user.username
        card.title=request.POST.get('title')
        card.text=request.POST.get('text')
        card.time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        #result['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        card.comments='0'
        try:
            image=request.FILES.get('images')
            #image.name=str(username)+'.jpg'
            if image.size>10000 and image.size<20480000:
                path=default_storage.save('Pet/static/images/BlogImages/'+image.name,ContentFile(image.read()))
                #tmp_file=os.path.join(settings.BASE_DIR,path)
                card.picture='/static/images/BlogImages/'+image.name
            else:
                #return HttpResponse("<p>图片应在2M之内！</p>")
                return HttpResponse("<script>  alert(\"图片应在2M之内!\"); window.location.href=\"/Pet/poster\" </script>")
        except:
            #return HttpResponse("<p>Error!</p>")
            return HttpResponse("<script>  alert(\"请存入图片!\"); window.location.href=\"/Pet/poster\" </script>")
        card.save()
        #return render(request,"index.html",ctx)
        return HttpResponse("<script>  alert(\"发帖成功！请等待审核。\"); window.location.href=\"/Pet/forum\" </script>")
    else:
        return redirect("/Account/login-2")

def forum(request):
    result={}
    list = Card.objects.all().order_by("-id")
    result['picture1']=list[0].picture
    result['time1']=list[0].time
    result['postname1']=list[0].postname
    result['comments1']=list[0].comments
    result['title1']=list[0].title
    result['text1']=list[0].text

    result['picture2']=list[1].picture
    result['time2']=list[1].time
    result['postname2']=list[1].postname
    result['comments2']=list[1].comments
    result['title2']=list[1].title
    result['text2']=list[1].text

    result['picture3']=list[2].picture
    result['time3']=list[2].time
    result['postname3']=list[2].postname
    result['comments3']=list[2].comments
    result['title3']=list[2].title
    result['text3']=list[2].text

    result['picture4']=list[3].picture
    result['time4']=list[3].time
    result['postname4']=list[3].postname
    result['comments4']=list[3].comments
    result['title4']=list[3].title
    result['text4']=list[3].text

    result['picture5']=list[4].picture
    result['time5']=list[4].time
    result['postname5']=list[4].postname
    result['comments5']=list[4].comments
    result['title5']=list[4].title
    result['text5']=list[4].text

    result['picture6']=list[5].picture
    result['time6']=list[5].time
    result['postname6']=list[5].postname
    result['comments6']=list[5].comments
    result['title6']=list[5].title
    result['text6']=list[5].text
    return render(request,"forum.html",result)

def search(request):
    result={}
    list = Card.objects.all().filter(postname=request.GET['keywords']).order_by("-id")
    try:
        result['picture1']=list[0].picture
        result['time1']=list[0].time
        result['postname1']=list[0].postname
        result['comments1']=list[0].comments
        result['title1']=list[0].title
        result['text1']=list[0].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[1].picture
        result['time2']=list[1].time
        result['postname2']=list[1].postname
        result['comments2']=list[1].comments
        result['title2']=list[1].title
        result['text2']=list[1].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[2].picture
        result['time3']=list[2].time
        result['postname3']=list[2].postname
        result['comments3']=list[2].comments
        result['title3']=list[2].title
        result['text3']=list[2].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[3].picture
        result['time4']=list[3].time
        result['postname4']=list[3].postname
        result['comments4']=list[3].comments
        result['title4']=list[3].title
        result['text4']=list[3].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[4].picture
        result['time5']=list[4].time
        result['postname5']=list[4].postname
        result['comments5']=list[4].comments
        result['title5']=list[4].title
        result['text5']=list[4].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[5].picture
        result['time6']=list[5].time
        result['postname6']=list[5].postname
        result['comments6']=list[5].comments
        result['title6']=list[5].title
        result['text6']=list[5].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)

def forum_page1(request):
    result={}
    list = Card.objects.all().order_by("-id")
    try:
        result['picture1']=list[0].picture
        result['time1']=list[0].time
        result['postname1']=list[0].postname
        result['comments1']=list[0].comments
        result['title1']=list[0].title
        result['text1']=list[0].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[1].picture
        result['time2']=list[1].time
        result['postname2']=list[1].postname
        result['comments2']=list[1].comments
        result['title2']=list[1].title
        result['text2']=list[1].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[2].picture
        result['time3']=list[2].time
        result['postname3']=list[2].postname
        result['comments3']=list[2].comments
        result['title3']=list[2].title
        result['text3']=list[2].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[3].picture
        result['time4']=list[3].time
        result['postname4']=list[3].postname
        result['comments4']=list[3].comments
        result['title4']=list[3].title
        result['text4']=list[3].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[4].picture
        result['time5']=list[4].time
        result['postname5']=list[4].postname
        result['comments5']=list[4].comments
        result['title5']=list[4].title
        result['text5']=list[4].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[5].picture
        result['time6']=list[5].time
        result['postname6']=list[5].postname
        result['comments6']=list[5].comments
        result['title6']=list[5].title
        result['text6']=list[5].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)

def forum_page5(request):
    result={}
    list = Card.objects.all().order_by("-id")
    try:
        result['picture1']=list[24].picture
        result['time1']=list[24].time
        result['postname1']=list[24].postname
        result['comments1']=list[24].comments
        result['title1']=list[24].title
        result['text1']=list[24].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[25].picture
        result['time2']=list[25].time
        result['postname2']=list[25].postname
        result['comments2']=list[25].comments
        result['title2']=list[25].title
        result['text2']=list[25].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[26].picture
        result['time3']=list[26].time
        result['postname3']=list[26].postname
        result['comments3']=list[26].comments
        result['title3']=list[26].title
        result['text3']=list[26].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[27].picture
        result['time4']=list[27].time
        result['postname4']=list[27].postname
        result['comments4']=list[27].comments
        result['title4']=list[27].title
        result['text4']=list[27].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[28].picture
        result['time5']=list[28].time
        result['postname5']=list[28].postname
        result['comments5']=list[28].comments
        result['title5']=list[28].title
        result['text5']=list[28].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[29].picture
        result['time6']=list[29].time
        result['postname6']=list[29].postname
        result['comments6']=list[29].comments
        result['title6']=list[29].title
        result['text6']=list[29].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)

def forum_page3(request):
    result={}
    list = Card.objects.all().order_by("-id")
    try:
        result['picture1']=list[12].picture
        result['time1']=list[12].time
        result['postname1']=list[12].postname
        result['comments1']=list[12].comments
        result['title1']=list[12].title
        result['text1']=list[12].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[13].picture
        result['time2']=list[13].time
        result['postname2']=list[13].postname
        result['comments2']=list[13].comments
        result['title2']=list[13].title
        result['text2']=list[13].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[14].picture
        result['time3']=list[14].time
        result['postname3']=list[14].postname
        result['comments3']=list[14].comments
        result['title3']=list[14].title
        result['text3']=list[14].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[15].picture
        result['time4']=list[15].time
        result['postname4']=list[15].postname
        result['comments4']=list[15].comments
        result['title4']=list[15].title
        result['text4']=list[15].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[16].picture
        result['time5']=list[16].time
        result['postname5']=list[16].postname
        result['comments5']=list[16].comments
        result['title5']=list[16].title
        result['text5']=list[16].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[17].picture
        result['time6']=list[17].time
        result['postname6']=list[17].postname
        result['comments6']=list[17].comments
        result['title6']=list[17].title
        result['text6']=list[17].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)

def forum_page4(request):
    result={}
    list = Card.objects.all().order_by("-id")
    try:
        result['picture1']=list[18].picture
        result['time1']=list[18].time
        result['postname1']=list[18].postname
        result['comments1']=list[18].comments
        result['title1']=list[18].title
        result['text1']=list[18].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[19].picture
        result['time2']=list[19].time
        result['postname2']=list[19].postname
        result['comments2']=list[19].comments
        result['title2']=list[19].title
        result['text2']=list[19].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[20].picture
        result['time3']=list[20].time
        result['postname3']=list[20].postname
        result['comments3']=list[20].comments
        result['title3']=list[20].title
        result['text3']=list[20].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[21].picture
        result['time4']=list[21].time
        result['postname4']=list[21].postname
        result['comments4']=list[21].comments
        result['title4']=list[21].title
        result['text4']=list[21].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[22].picture
        result['time5']=list[22].time
        result['postname5']=list[22].postname
        result['comments5']=list[22].comments
        result['title5']=list[22].title
        result['text5']=list[22].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[23].picture
        result['time6']=list[23].time
        result['postname6']=list[23].postname
        result['comments6']=list[23].comments
        result['title6']=list[23].title
        result['text6']=list[23].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)

def forum_page2(request):
    result={}
    list = Card.objects.all().order_by("-id")
    try:
        result['picture1']=list[6].picture
        result['time1']=list[6].time
        result['postname1']=list[6].postname
        result['comments1']=list[6].comments
        result['title1']=list[6].title
        result['text1']=list[6].text
    except:
        result['picture1']='/static/images/BlogImages/g7.jpg'
        result['time1']="NULL"
        result['postname1']="NULL"
        result['comments1']="0"
        result['title1']="NULL"
        result['text1']="NULL"
    try:
        result['picture2']=list[7].picture
        result['time2']=list[7].time
        result['postname2']=list[7].postname
        result['comments2']=list[7].comments
        result['title2']=list[7].title
        result['text2']=list[7].text
    except:
        result['picture2']='/static/images/BlogImages/g7.jpg'
        result['time2']="NULL"
        result['postname2']="NULL"
        result['comments2']="0"
        result['title2']="NULL"
        result['text2']="NULL"
    try:
        result['picture3']=list[8].picture
        result['time3']=list[8].time
        result['postname3']=list[8].postname
        result['comments3']=list[8].comments
        result['title3']=list[8].title
        result['text3']=list[8].text
    except:
        result['picture3']='/static/images/BlogImages/g7.jpg'
        result['time3']="NULL"
        result['postname3']="NULL"
        result['comments3']="0"
        result['title3']="NULL"
        result['text3']="NULL"
    try:
        result['picture4']=list[9].picture
        result['time4']=list[9].time
        result['postname4']=list[9].postname
        result['comments4']=list[9].comments
        result['title4']=list[9].title
        result['text4']=list[9].text
    except:
        result['picture4']='/static/images/BlogImages/g7.jpg'
        result['time4']="NULL"
        result['postname4']="NULL"
        result['comments4']="0"
        result['title4']="NULL"
        result['text4']="NULL"
    try:
        result['picture5']=list[10].picture
        result['time5']=list[10].time
        result['postname5']=list[10].postname
        result['comments5']=list[10].comments
        result['title5']=list[10].title
        result['text5']=list[10].text
    except:
        result['picture5']='/static/images/BlogImages/g7.jpg'
        result['time5']="NULL"
        result['postname5']="NULL"
        result['comments5']="0"
        result['title5']="NULL"
        result['text5']="NULL"
    try:
        result['picture6']=list[11].picture
        result['time6']=list[11].time
        result['postname6']=list[11].postname
        result['comments6']=list[11].comments
        result['title6']=list[11].title
        result['text6']=list[11].text
    except:
        result['picture6']='/static/images/BlogImages/g7.jpg'
        result['time6']="NULL"
        result['postname6']="NULL"
        result['comments6']="0"
        result['title6']="NULL"
        result['text6']="NULL"
    return render(request,"forum.html",result)