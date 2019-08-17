from django.shortcuts import render
from .models import Service #accediento al modelo o a la base de datos
# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html",{'services': services})
    