########### admin_app.urls.py############
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/login$',views.admin_process_login),
    url(r'^login_success$',views.login_success),
    url(r'^change_password',views.change_password),
    url(r'^process/change_password$', views.process_change_password),
    url(r'^manage_admins$', views.manage_admins),
    url(r'^add_admin$', views.add_admin),
    url(r'^process/add_admin$', views.process_add_admin),
    url(r'^delete/(?P<admin_id>\d+)$', views.delete_an_admin),
    url(r'^reset_password/(?P<admin_id>\d+)$', views.reset_password),
    url(r'^logout$',views.logout),
    url(r'^manage_courses$', views.manage_courses),
    url(r'^add_course$', views.add_course),
    url(r'^process/add_course$',views.process_add_course),
    url(r'^delete_course/(?P<course_id>\d+)$',views.delete_course),
   
]
