from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # object_list = list(Student.objects.all()) # так будет 6 забросов
    object_list = list(Student.objects.prefetch_related('teachers')) # так всего 4 запроса
    context = {'object_list': object_list}

    return render(request, template, context)
