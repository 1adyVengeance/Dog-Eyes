from django.conf.urls import url,include
from django.contrib import admin

from material import views

urlpatterns = [
    url(r'^$', views.show_all_material_type),
]