from django.shortcuts import render, redirect
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination

""" for meat """


class MainMenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.meat
        fields = "__all__"


def meat(request):
    queryset = models.meat.objects.all()

    return render(request, 'Ingrem.html', {"queryset": queryset})


def madd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredientm/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


""" for vegetable """


class MainMenuModelForm_veg(BootStrapModelForm):
    class Meta:
        model = models.vegetable
        fields = "__all__"


def veg(request):
    queryset = models.vegetable.objects.all()

    return render(request, 'Ingrev.html', {"queryset": queryset})


def vadd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_veg()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_veg(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredientv/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


""" for Auxiliary"""


class MainMenuModelForm_aux(BootStrapModelForm):
    class Meta:
        model = models.Auxiliary
        fields = "__all__"


def aux(request):
    queryset = models.Auxiliary.objects.all()

    return render(request, 'Ingrea.html', {"queryset": queryset})


def aadd(request):
    """ Add meat ingredient """
    title = "Create your new meat ingredient"
    if request.method == 'GET':
        form = MainMenuModelForm_aux()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm_aux(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/Ingredienta/')
    return render(request, 'upload_form.html', {"form": form, "title": title})
