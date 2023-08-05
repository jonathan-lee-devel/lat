from uuid import uuid4

from django.db import models

UUID4_MAX_LENGTH = 36


class Job(models.Model):
    uuid = models.CharField(primary_key=True, max_length=UUID4_MAX_LENGTH, default=uuid4)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_created=True)


class Build(models.Model):
    uuid = models.CharField(primary_key=True, max_length=UUID4_MAX_LENGTH, default=uuid4)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_created=True)
