from django.conf.urls import url
from django.contrib import admin

from product import views

urlpatterns = [
    url(r'^products_list/', views.products_list, name='products_list'),
    url(r'^goods_type/', views.goods_type, name='goods_type'),
    url(r'^recipe/', views.recipe, name='recipe'),
    url(r'^product_update/.*$', views.product_update, name='product_update'),
    url(r'^goods_type_update/.*$', views.goods_type_update, name='goods_type_update'),
    url(r'^recipe_update/.*$', views.recipe_update, name='recipe_update')
]