from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *

def home(request):

    return render(request, 'home.html', {})

def createCoffee(request):
    context = {}
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        context['form']=form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m()
            return redirect("home")
        else:
            return render(request, 'createCoffee.html', context)
    else:
        form = CoffeeForm()
        context['form']=form
        return render(request, 'createCoffee.html', context)

def editCoffee(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee']=coffee
    if request.method == "POST":
        form = CoffeeForm(request.POST,instance=coffee)
        context['form']=form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m()
            return redirect("home")
        else:
            return render(request, 'editCoffee.html', context)
    else:
        form = CoffeeForm(instance=coffee)
        context['form']=form
        return render(request, 'editCoffee.html', context)


def createBean(request):
    context = {}
    if request.method == "POST":
        form = BeanForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'createBean.html', context)
    else:
        form = BeanForm()
        context['form']=form
        return render(request, 'createBean.html', context)

def editBean(request, bean_id):
    context = {}
    bean = Bean.objects.get(id=bean_id)
    context['bean']=bean
    if request.method == "POST":
        form = BeanForm(request.POST,instance=bean)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, 'editBean.html', context)
    else:
        form = BeanForm(instance=bean)
        context['form']=form
        return render(request, 'editBean.html', context)

def deleteBean(request, bean_id):
    Bean.objects.get(id=bean_id).delete()
    return redirect("home")
