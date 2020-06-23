from django.shortcuts import render
from django.http import HttpResponse
from .models import Name


def index(request):
    return render(request, "hello.html")


def saveToDb(request):
    try:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        Name.objects.create(fullname=fullname, email=email, address=address)
        count = Name.objects.count()
    except Exception as err:
        count = 0
    names = Name.objects.all()
    return render(request, "data.html", {'names': names})
