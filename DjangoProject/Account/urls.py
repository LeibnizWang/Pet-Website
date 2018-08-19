#coding:utf-8
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
import views,tests

urlpatterns=[
    url(r'^$',views.help),
    #联系我们
    url(r'^contact$',views.contact),
    url(r'^contact-submit$',views.contact_submit),
    #创建账户
    url(r'^create-account$',views.create_account),
    url(r'^create-account-submit$',views.create_account_submit),
    #忘记密码
    url(r'^forgot-password$',views.forgot_password),
    #登录
    url(r'^login-1$',views.login_1),
    url(r'^login-submit$',views.login_submit),
    url(r'^login-2$',views.login_2),
    url(r'^login-submit-new$',views.login_submit_new),
    url(r'^payment-form$',views.payment_form),
    #url(r'^create$',tests.create),
    url(r'^userlogout$',views.userlogout),
    #修改密码
    url(r'^change-submit$',views.change_submit),

]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)