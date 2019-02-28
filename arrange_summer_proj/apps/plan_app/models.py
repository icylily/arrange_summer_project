from django.db import models
import re
import bcrypt
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

        # release_date = datetime.strptime(postData["release_date"], '%Y-%m-%d')
        # recent_date = datetime.now()
        # if release_date > recent_date:
        #     errors["release_date"] = "Release date should be in the past"
        # if len(self.filter(title=postData["title"])) > 0:
        #     errors["existed"] = "This  title already existed!"
        return errors

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=255)
    user_created_by = models.ForeignKey(
        "login_app.User", related_name="created_plans")
    included_courses = models.ManyToManyField(
        "course_app.Course", related_name="referenced_courses")
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
