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


def process_add_plan(request):
    if not("logined" in request.session):
        return redirect("/success")
    current_user = User.objects.get(id=int(request.session["current_user"]))
    Plan.objects.create(
        name=request.POST["name"], description=request.POST["description"], user_created_by=current_user)
    return redirect("/success")

