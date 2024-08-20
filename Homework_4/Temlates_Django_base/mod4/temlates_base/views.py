from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/base.html')


def page1(request):
    return render(request, 'page/page_1.html')


def page2(request):
    return render(request, 'page/page_2.html')


def page3(request):
    return render(request, 'page/page_3.html')



