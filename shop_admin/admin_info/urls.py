from django.conf.urls import url

from admin_info import views

urlpatterns = [
    url(r'^users/', views.get_admins),
    url(r'^user/$', views.get_admin_info),
    url(r'^user/all/', views.show_all_admin),
    url(r'^user/(?P<id>[0-9]+)/', views.get_admin_by_id),
    url(r'^user/change/', views.change_admin_info),
    url(r'^user/change_status/', views.change_admin_status),
    url(r'^user/change_passwd/', views.change_admin_passwd),
    url(r'^user/role/(?P<role_id>[0-9]+)/', views.get_admin_by_role_id),

    url(r'^role/all/', views.show_all_role),
    url(r'^role/(?P<role_id>[0-9]+)/', views.get_role_by_id),
    url(r'^role/change/', views.change_role),

    url(r'^power/all/', views.show_all_power),
    url(r'^power/(?P<power_id>[0-9]+)/', views.get_power_by_id),
    url(r'^power/change/', views.change_power),
    url(r'^power/role/(?P<role_id>[0-9]+)/', views.get_power_by_role_id),

]