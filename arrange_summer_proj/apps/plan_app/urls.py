####### plan_app ########

from django.conf.urls import url, include
from . import views

urlpatterns = [
    
    url(r'^plan_create$', views.create_plan),
    # delete_course_from_plan/1/1
    url(r'^delete_course_from_plan/(?P<plan_id>\d+)/(?P<course_id>\d+)$',
        views.delete_course_from_plan),
]
