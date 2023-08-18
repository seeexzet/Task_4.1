from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV) as f:
        reader = csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel')
        for row in reader:
            print(row['first_name'], row['last_name'])


    context = {
    #     'bus_stations': ...,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)
