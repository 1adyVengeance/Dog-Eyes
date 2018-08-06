from django.conf.urls import url
from django.contrib import admin

from admin_user import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^products_list/', views.products_list, name='products_list')
]