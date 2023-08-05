from django.contrib import admin

from .models import Job, Build

admin.site.register(Job)
admin.site.register(Build)
