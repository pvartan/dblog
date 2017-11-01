"""Определяет схемы URL для learning_logs."""
from django.conf.urls import url
from . import views


urlpatterns = [
        # Домашняя страница
        url(r'^$', views.index, name='index'),

        #страница со списком блогов
        url(r'^blogs$', views.blogs, name='blogs'),

        #страница с отдельными страницами блога
        url(r'^blogs/(?P<blog_id>\d+)/$', views.blog, name='blog'),

        #создание записи в блоге
        url(r'^new_blog$', views.new_blog, name='new_blog'),

        #редактирование блога
        url(r'^edit_blog/(?P<blog_id>\d+)/$', views.edit_blog,  name='edit_blog'),

        #mymmy
        url(r'^mymy$', views.mymy, name='mymy'),

        #datetime
        url(r'^me$', views.me, name='me'),
        ]

