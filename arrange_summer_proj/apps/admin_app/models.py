################### admin_app.models.py #######################


# Create your models here.
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["username"]) < 5:
            errors["username"] = "Admin's username should be at least 5 characters."
        if len(postData["password"]) < 8:
            errors["password"] = "Passworsd should be at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Please re-enter the same password!"
        if len(self.filter(username=postData["username"])) > 0:
            errors["username"] = "This  admin already existed!"

        # release_date = datetime.strptime(postData["release_date"], '%Y-%m-%d')
        # recent_date = datetime.now()
        # if release_date > recent_date:
        #     errors["release_date"] = "Release date should be in the past"
        # if len(self.filter(title=postData["title"])) > 0:
        #     errors["existed"] = "This  title already existed!"
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData["username"]) < 5:
            errors["login_em"] = "Please input a vilid email address."
            return errors
        if len(self.filter(username=postData["username"])) < 1:
            errors["login_em"] = "No such admin ,please re-enter another one !"
            return errors
        if bcrypt.checkpw(postData["password"].encode(), self.filter(username=postData["username"])[0].password.encode()) != True:
            errors["login_pass"] = "password encorrect"
        return errors

    def change_password_validator(self, postData):
        errors = {}
        
        if bcrypt.checkpw(postData["current_password"].encode(), self.filter(username=postData["username"])[0].password.encode()) != True:
            errors["current_password"] = "password encorrect"
        
        if len(postData["new_password"]) < 8:
            errors["new_password"] = "Passworsd should be at least 8 characters"
        if postData["new_password"] != postData["confirm_password"]:
            errors["confirm_password"] = "Please re-enter the same password!"
        return errors

class Admin(models.Model):
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    admin_type = models.IntegerField() # 1 means super admin, 2 means normal admin
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    objects = ShowManager()
