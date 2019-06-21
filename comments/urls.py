from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'comments'
urlpatterns = [
   url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name="post_comment"),
]