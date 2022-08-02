from django.shortcuts import render
from app01 import models


def page(request):
    queryset = models.home.objects.all()
    return render(request, 'category.html', {"queryset": queryset})
