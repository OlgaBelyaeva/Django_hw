from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='') as f:
        bus_stations = list(csv.DictReader(f))
    paginator = Paginator(bus_stations, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)




