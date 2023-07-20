from django.shortcuts import render
from .models import Town
import random

def home(request):
    return render(request, 'home.html')

def list(request):
    items = Town.objects.all()
    context = {'items':items}
    return render(request, 'items.html', context)

s = ["Spa", "Zandvoort", "Jeddah"]
def create(request):
    random_index = random.randint(0, len(s) - 1)
    d = Town.objects.create(id=random.randint(30,1000))
    d.c_name = s[random_index]
    d.c_aeroport_index = "One"
    d.c_car_number = "Two"
    d.save()
    items = Town.objects.all()
    context = {'items':items}
    return render(request, 'updated.html', context)