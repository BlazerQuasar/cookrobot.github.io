from django.http import HttpResponseRedirect

from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
import tkinter.messagebox
from tkinter import *
from django.contrib import messages
from django.shortcuts import render, redirect
from app01 import models


# My favorite
def fav_meun(request, nid):
    """ Favorite Menu list """
    queryset = models.home.objects.filter(id=nid)
    for info in queryset:
        name = info.name
        tem = info.temperature
        time = info.time
        ute = info.utensils
        cate = info.cate
        des = info.description
        meat = info.meat
        au = info.auxiliary
        veg = info.veg
        step = info.steps
        rate = info.rate
        cal = info.calories
        img = info.img
        context = {
            "name": name,
            "temperature": tem,
            "time": time,
            "utensils": ute,
            "cate": cate,
            "description": des,
            "meat": meat,
            "auxiliary": au,
            "veg": veg,
            "steps": step,
            "rate": rate,
            "calories": cal,
            "img": img,
        }
        judge = models.favorite.objects.values_list('name', flat=True)

        if context['name'] in judge:
            messages.error(request, 'The data already exists')

            return HttpResponseRedirect('/main/')

        queryset1 = models.favorite.objects.create(**context)

        queryset2 = models.favorite.objects.all()

        return render(request, 'meun_list.html', {"queryset2": queryset2})


def fav_list(request):
    search_data = request.GET.get('q', "")

    queryset2 = models.favorite.objects.filter(name__icontains=search_data)
    if queryset2:
        page_object = Pagination(request, queryset2)
        context = {
            "search_data": search_data,
            "queryset2": page_object.page_queryset,
            "page_string": page_object.html(),
        }
        return render(request, 'meun_list.html', context)

    queryset2 = models.favorite.objects.filter(calories__icontains=search_data)

    page_object = Pagination(request, queryset2)
    context = {
        "search_data": search_data,
        "queryset2": page_object.page_queryset,
        "page_string": page_object.html(),
    }

    return render(request, 'meun_list.html', context)

    # queryset2 = models.favorite.objects.all()
    # return render(request, 'meun_list.html', {"queryset2": queryset2})


def fav_dele(request, nid):
    models.favorite.objects.filter(id=nid).delete()
    return redirect('/meun/list/')


def fav_cook(request, nid):
    queryset = models.favorite.objects.filter(id=nid)
    tools = int(request.POST.get("tools"))
    return render(request, 'sec_menu1.html', {"queryset": queryset, "tools": tools})
