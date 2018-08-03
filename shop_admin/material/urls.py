from django.conf.urls import url,include
from django.contrib import admin

from material import views

urlpatterns = [
    url(r'^type/all/', views.show_all_material_type),
    url(r'^type/(?P<id>[0-9]+)/', views.get_material_type_by_id),
    url(r'^type/change/', views.change_material_type_info),
    url(r'info/all/', views.show_all_material),
    url(r'info/type/(?P<type_id>[0-9]+)/', views.get_materials_by_type),
    url(r'info/(?P<id>[0-9]+)/', views.get_material_by_id),
    url(r'info/change/', views.change_material_info),
]