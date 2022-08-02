from app01.utils.pagination import Pagination
from openpyxl import load_workbook
from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django.views.decorators.csrf import csrf_exempt


def page(request):
    """ Most popular """

    queryset = models.home.objects.filter(cate=1)

    return render(request, 'subpage1.html', {"queryset": queryset})


def page2(request):
    """ Best taste """
    queryset = models.home.objects.filter(cate=2)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page3(request):
    """ VEGETARIANISM"""
    queryset = models.home.objects.filter(cate=3)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page4(request):
    """ Gorgeous """
    queryset = models.home.objects.filter(cate=4)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page5(request):
    """ Fast Food """
    queryset = models.home.objects.filter(cate=5)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page6(request):
    """ Breakfast """
    queryset = models.home.objects.filter(cate=6)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page7(request):
    """ Homely recipes """
    queryset = models.home.objects.filter(cate=7)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page8(request):
    """ Baking """
    queryset = models.home.objects.filter(cate=8)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page9(request):
    """ Child's food"""
    queryset = models.home.objects.filter(cate=9)
    return render(request, 'subpage1.html', {"queryset": queryset})

def page10(request):
    """ Recommand """
    queryset = models.home.objects.filter(cate=9)
    return render(request, 'subpage1.html', {"queryset": queryset})

def page11(request):
    """ Staple food"""
    queryset = models.home.objects.filter(cate=11)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page12(request):
    """ Dessert food"""
    queryset = models.home.objects.filter(cate=12)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page13(request):
    """ Snack food"""
    queryset = models.home.objects.filter(cate=13)
    return render(request, 'subpage1.html', {"queryset": queryset})


def page14(request):
    """ Western food"""
    queryset = models.home.objects.filter(cate=14)
    return render(request, 'subpage1.html', {"queryset": queryset})