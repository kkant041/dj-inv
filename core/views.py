from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from .models import prodDir, transHis

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def signupView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('orders:index')

    else:
        form = SignUpForm()
        return render(request, "accounts/signup.html", {'form': form})


def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('orders:index')
        else:
            return render(request, "accounts/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "accounts/login.html")


def allProd(request):
    username = request.user.username
    context = {
        'products': prodDir.objects.all().get(username=username)
    }
    return render(request, 'main/allProd.html', context)


def modifyProd(request):
    username = request.user.username
    context = {
        'products': prodDir.objects.all().get(username=username)
    }
    return render(request, 'main/modifyProd.html', context)

def addProd(request):
    username = request.user.username
    context = {
        'products': prodDir.objects.all().get(username=username)
    }
    return render(request, 'main/addProd.html', context)

def remProd(request):
    username = request.user.username
    context = {
        'products': prodDir.objects.all().get(username=username)
    }
    return render(request, 'main/remProd.html', context)


def transHisView(request):
    username = request.user.username
    context = {
        'hisData': transHis.objects.all().get(username=username)
    }
    return render(request, 'main/transHis.html', context)
