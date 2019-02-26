########### admin_app.urls.py############
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/login$',views.admin_process_login),
    url(r'^login_success$',views.login_success),
    url(r'^change_password',views.change_password),
    url(r'^process/change_password$', views.process_change_password),
   
]
