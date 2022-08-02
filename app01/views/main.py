from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
from django import forms
from django.shortcuts import render, redirect
from app01 import models


class MainMenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.home
        fields = "__all__"
        # exclude = ["id"]


# Main menu
def home(request):
    # # Search function

    search_data = request.GET.get('q', "")

    queryset = models.home.objects.filter(name__icontains=search_data)
    if queryset:
        page_object = Pagination(request, queryset)
        context = {
            "search_data": search_data,
            "queryset": page_object.page_queryset,
            "page_string": page_object.html(),
        }
        return render(request, 'main.html', context)

    queryset = models.home.objects.filter(calories__icontains=search_data)

    page_object = Pagination(request, queryset)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'main.html', context)


def main_menu_add(request):
    """ Add the menu in main page """
    title = "Create your new menu"
    if request.method == 'GET':
        form = MainMenuModelForm()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MainMenuModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/main/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


# Second menu
class MenuModelForm(BootStrapModelForm):
    class Meta:
        model = models.Menu
        fields = "__all__"
        # exclude = ["id"]


def add_meun(request):
    title = "Create menu"
    if request.method == 'GET':
        form = MenuModelForm()

        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = MenuModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/meun/list/')
    return render(request, 'upload_form.html', {"form": form, "title": title})


def edit_meun(request, nid):
    """ Edit """
    if request.method == 'GET':
        row_object = models.Menu.objects.filter(id=nid).first()
        form = MenuModelForm(instance=row_object)
        return render(request, 'meun_edit.html', {"form": form})

    row_object = models.Menu.objects.filter(id=nid).first()

    form = MenuModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/meun/list/')
    return render(request, 'meun_edit.html', {"form": form})


def delete_meun(request, nid):
    models.home.objects.filter(id=nid).delete()
    return redirect('/meun/list/')
