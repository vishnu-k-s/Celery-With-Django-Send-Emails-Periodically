from celery import schedules
from celery.schedules import crontab
from django.shortcuts import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .tasks import send_mail_func

# Create your views here.
def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Mail sent sucessfully')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 11, minute = 8)
    task = PeriodicTask.objects.create(crontab = schedule, name = 'schedule_mail_2', task = 'send_mail.tasks.send_mail_func')
    return HttpResponse('Mail sent sucessfully')