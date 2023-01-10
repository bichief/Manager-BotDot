import datetime

from django.shortcuts import render
from django.utils import timezone

from admin_panel.telebot.models import Manager, Client


def statistics(request):
    template = 'statistics/index.html'
    now = timezone.now()
    date = datetime.datetime.today()
    week = date.strftime("%V")

    count_managers = Manager.objects.all().count()
    count_clients = Client.objects.all().count()
    context = {
        'count_managers': count_managers,
        'count_clients': count_clients
    }

    return render(request, template, context)


