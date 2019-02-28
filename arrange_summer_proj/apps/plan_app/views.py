######## plan_app.views.py #####


from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from apps.login_app.models import User
from apps.course_app.models import Course

# Create your views here.
def create_plan(request):

    return render(request,"plan_app/create_plan.html")


def delete_course_from_plan(request,plan_id,course_id):
    this_plan = Plan.objects.get(id=int(plan_id))
    this_course = Course.objects.get(id=int(course_id))
    this_plan.included_courses.remove(this_course)
    return redirect('/success')