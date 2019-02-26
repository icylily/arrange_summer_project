######## admin_app.views.py #####


from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
from apps.login_app.models import User

# need to do
# from apps.course_app.models import Course
# from apps.plan_app.models import Plan
# from apps.admin_app import Admin

# Create your views here.
def index(request):
    if len(Admin.objects.all())==0:
        
        this_password = bcrypt.hashpw(
            '12345678'.encode(), bcrypt.gensalt())
        # this_password = request.POST["password"]
        super_admin = Admin.objects.create(
            username="Super_Admin",  password=this_password,admin_type=1)
        print(super_admin)

    return render(request,"admin_app/index.html")
    # return render(request, "login_app/index.html")


def admin_process_login(request):
    # return HttpResponse("admin_process_login")
    errors = Admin.objects.login_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            print(messages)
        # redirect the user back to the form to fix the errors
        return redirect('/admin')
    else:
        #set session
        this_admin = Admin.objects.filter(username=request.POST["username"])
        request.session["logined"] = "yes"
        request.session["logined_type"] = this_admin[0].admin_type  #1 super admin,2 normal admin,3 normal user
        request.session["username"] = this_admin[0].username
        request.session["source"] = 'login'
        return redirect("/admin/login_success")


def process_change_password(request):
    errors = Admin.objects.change_password_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            print(messages)
        # redirect the user back to the form to fix the errors
        return redirect('/admin/login_success')
    else:
        #set session
        this_admin = Admin.objects.filter(username=request.POST["username"])[0]
        print("password is ",this_admin.password)
        this_password = bcrypt.hashpw(
            request.POST["new_password"].encode(), bcrypt.gensalt())
        
        this_admin.password = this_password
        this_admin.save()
        print(this_admin.password)
        request.session["source"] = "change_password_success"
        return redirect("/admin/login_success")


def login_success(request):
    

    return  render(request,"admin_app/admin_dashboard1.html")


def change_password(request):
    request.session["source"] = 'change_password'
    return redirect("/admin/login_success")
