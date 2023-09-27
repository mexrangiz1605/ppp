from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.contrib.auth.models import User


# Create your views here.



def index(request):
    return render(request,'index.html')


def firstfood(request):
    foods = Food.objects.all()
    context = {'foods':foods}
    return render(request, 'firstfood.html', context)


def secondfood(request):
    meals = Secondfood.objects.all()
    context = {'meals':meals}
    return render(request, "secondfood.html", context)


def fastfood(request):
    fast = Fastfood.objects.all()
    context = {'fast':fast}
    return render(request, "fastfood.html", context)


def desert(request):
    deserts = Desert.objects.all()
    context = {'deserts':deserts}
    return render(request, "desert.html", context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    context = {'form':form}
    return render(request, 'contact.html', context)