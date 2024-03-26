from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def page1(request):
    return render(request,"webSite_TBBT\home.html")

def page2(request):
    return render(request,"webSite_TBBT\cast.html")

def page3(request):
    return render(request,"webSite_TBBT\spinOff.html")