################## course_app.models############
from django.db import models
# import re

from datetime import datetime



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(postData["destination"]) < 3:
        #     errors["destination"] = "Destination should be at least 3 character."
        # if len(postData["plan"]) < 3:
        #     errors["plan"] = "Description should be at least 3 characters."
        # start_date = datetime.strptime(postData["start_date"], '%Y-%m-%d')
        # end_date = datetime.strptime(postData["end_date"], '%Y-%m-%d')
        # recent_date = datetime.now()
        # if start_date < recent_date:
        #     errors["start_date"] = "Start date should be in the furture"
        # if end_date < start_date:
        #     errors["end_date"] = "End date should not be before the start date."

        return errors

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_age = models.IntegerField()
    end_age = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True)
    admin_created_by = models.ForeignKey(
        "admin_app.Admin", related_name="created_courses")
    users_who_registered = models.ManyToManyField(
        "login_app.User", related_name="registered_courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


