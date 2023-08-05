from django.http import JsonResponse

from jenkins.models import Job


def index(request):
    jobs = list(Job.objects.values('name', 'date_added'))
    return JsonResponse({'jobs': jobs})
