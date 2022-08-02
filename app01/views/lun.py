from django.shortcuts import render


def page1(request):
    return render(request, 'det_lun1.html')


def page2(request):
    return render(request, 'det_lun2.html')


def page3(request):
    return render(request, 'det_lun3.html')
