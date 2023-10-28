from hashlib import sha256
from django.shortcuts import render
from .models import User, Birds, ViewedUser
from django.contrib.auth import authenticate
"""
Основные функции:
auth - процесс аутентфикации пользователя.


"""


def auth(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        pswHash = sha256(password.encode('utf-8')).hexdigest()
        user = User.objects.filter(login=login, password=password)
        if user:  # Если логин и пароль существуют, то переходим на основную форму, это процесс авторизации.
            return render(request, 'viewBirds.html/', {"login": login})
        elif login is not None:
            ErorrMessage = "Incorrect username or password."
            return render(request, 'auth.html/', {"Error": ErorrMessage})
    return render(request, 'auth.html/')



#def userView(request):


def rgstrUser(request):
    if request.method == 'POST':
        user = User()
        user.login = request.POST.get("login")
        user.password = request.POST.get("password")
        user.mail = request.POST.get("email")
        return render(request, '/')


def viewBirds(request):
    birds = Birds.objects.all()
    return render(request, 'viewBirds.html/', {"birds": birds})


def creatBirds(request):
    if request.method == 'POST':
        birds = Birds()
        birds.name = request.POST.get('name')
        birds.feather_color = request.POST.get('color')
        birds.PNG = request.POST.get('PNG')
        birds.save()
        return render(request, 'createBirds.html/')
    return render(request, 'createBirds.html/')
