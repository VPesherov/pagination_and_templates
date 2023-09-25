from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице



    with open(settings.BUS_STATION_CSV, newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        BUS_STATIONS = []
        for row in reader:
            BUS_STATIONS.append(row)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(BUS_STATIONS, 5)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
