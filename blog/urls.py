from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='blog'
urlpatterns = [
   # 文章的首页
   url(r"^index/$", views.index, name='index'),
   # 详情页
   url(r"^post/(?P<pk>[0-9]+)/$", views.detail, name="detail"),
   # 归档页
   url(r"^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$", views.archives, name="archives"),
   # 分类
   url(r"^category/(?P<pk>[0-9]+)/$", views.category, name="category"),
]