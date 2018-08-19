#coding:utf-8
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
import views,tests

urlpatterns=[
    url(r'^index$',views.index),
    url(r'^personal$',views.personal),
    url(r'^center$',views.center),
    #联系我们
    url(r'^contact$',views.contact),
    url(r'^contact-submit$',views.contact_submit),
    #寄养
    url(r'^fostering$',views.fostering),
    url(r'^fostering-submit$',views.fostering_submit),
    #收养
    url(r'^adoption$',views.adoption),
    url(r'^adoption-submit$',views.adoption_submit),
    #匹配结果
    #url(r'^match$',views.match),
    #url(r'^makesure$',views.makesure),
    url(r'^refresh$',views.refresh),
    url(r'^makesure1$',views.makesure1),
    url(r'^makesure2$',views.makesure2),
    url(r'^makesure3$',views.makesure3),
    url(r'^makesure4$',views.makesure4),
    url(r'^makesure5$',views.makesure5),
    url(r'^makesure6$',views.makesure6),
    url(r'^makesure7$',views.makesure7),
    url(r'^makesure8$',views.makesure8),
    url(r'^makesure1-submit$',views.makesure1_submit),
    url(r'^makesure2-submit$',views.makesure2_submit),
    url(r'^makesure3-submit$',views.makesure3_submit),
    url(r'^makesure4-submit$',views.makesure4_submit),
    url(r'^makesure5-submit$',views.makesure5_submit),
    url(r'^makesure6-submit$',views.makesure6_submit),
    url(r'^makesure7-submit$',views.makesure7_submit),
    url(r'^makesure8-submit$',views.makesure8_submit),

    url(r'^agree$',views.agree),
    url(r'^refuse$',views.refuse),
    url(r'^done$',views.done),
    #论坛
    url(r'^forum$',views.forum),
    url(r'^forum-page1$',views.forum_page1),
    url(r'^forum-page2$',views.forum_page2),
    url(r'^forum-page3$',views.forum_page3),
    url(r'^forum-page4$',views.forum_page4),
    url(r'^forum-page5$',views.forum_page5),
    url(r'^forum-search$',views.search),
    url(r'^poster$',views.poster),
    url(r'^poster-submit$',views.poster_submit),

]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)