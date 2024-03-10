from django.shortcuts import render

from django.http import HttpResponse


    

def home(request):
    return render(request,"projectHome.html")
def Nav(request):
    return render(request,"projectNabar.html")
def about(request):
    return render(request,"about.html")
def adminpage(request):
    return render(request,"adminpage.html")