from django.shortcuts import render

from jenkins.models import Job


def index(request):
    jobs = list(Job.objects.values('name', 'date_added'))
    return render(request, 'jenkins/index.html', context={'jobs': jobs})

