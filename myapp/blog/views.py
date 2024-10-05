from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect
def index(request):
    return render(request, "blogs/index.html")

def signup(request):
    return render(request, "blogs/signup.html")
    
def signin(request):
    return render(request, "blogs/signin.html")

def login(request):
    if request.POST:
        login = request.POST['login']
        parol1 = request.POST['parol1']
        user = authenticate(request,username=login, password=parol1)
        if user is None:
            return redirect(signup)
        else:
            return HttpResponse(f'salom')

def registation(request):
    if request.POST:
        ism = request.POST['ism']
        email = request.POST['email']
        login = request.POST['login']
        parol1 = request.POST['parol1']
        parol2 = request.POST['parol2']
        if parol1 == parol2 and ism and len(parol1)>7:
            user = User.objects.create_user(username=login, email=email, password=parol1)
            user.first_name = ism
            user.email = email
            user.username = login
            user.save
            return HttpResponse(f'salom')