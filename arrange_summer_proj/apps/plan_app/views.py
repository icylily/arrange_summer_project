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


def add_course(request,plan_id):
    this_plan = Plan.objects.get(id=int(plan_id))
    context = {
        "this_plan":this_plan,
        "other_courses": Course.objects.exclude(referenced_plans__id=int(plan_id)),
    }
    return render(request,"plan_app/add_course.html",context)


def add_course_to_plan(request,plan_id,course_id):
    this_plan = Plan.objects.get(id=int(plan_id))
    this_course = Course.objects.get(id=int(course_id))
    errors = {}
    for course in this_plan.included_courses.all():
        if (this_course.start_date < course.end_date) and(this_course.end_date>course.start_date):
            errors["course"] = "This course conflicted with a existed course."
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
                print(messages)
            return redirect("/plan/add_course/"+plan_id)
    this_plan.included_courses.add(this_course)        
    errors["success"] = "No conflict, added successfully'"
    for key, value in errors.items():
        messages.error(request, value, extra_tags=key)
        print(messages)
    return redirect("/plan/add_course/"+plan_id)
    

def delete_course1(request, plan_id, course_id):
    this_plan = Plan.objects.get(id=int(plan_id))
    this_course = Course.objects.get(id=int(course_id))
    this_plan.included_courses.remove(this_course)
    return redirect("/plan/add_course/"+plan_id)
