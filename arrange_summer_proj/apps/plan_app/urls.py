####### plan_app ########

from django.conf.urls import url, include
from . import views

urlpatterns = [
    
    url(r'^plan_create$', views.create_plan),
    # delete_course_from_plan/1/1
    url(r'^delete_course_from_plan/(?P<plan_id>\d+)/(?P<course_id>\d+)$',
        views.delete_course_from_plan),
    url(r'^process/add_plan$', views.process_add_plan),
    url(r'^add_course/(?P<plan_id>\d+)$',views.add_course),
    url(r'^add_course_to_plan/(?P<plan_id>\d+)/(?P<course_id>\d+)$',
        views.add_course_to_plan),
    url(r'^delete_course1/(?P<plan_id>\d+)/(?P<course_id>\d+)$',
        views.delete_course1),
    # / plan/calendar_view/{{plan.id}}
    url(r'^calendar_view/(?P<plan_id>\d+)$',views.calendar_view),
    url(r'^delete/(?P<plan_id>\d+)$', views.delete_plan),
]
