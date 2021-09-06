from django.db import models


class Employee(models.Model):
    regNo = models.TextField(unique=True)
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)