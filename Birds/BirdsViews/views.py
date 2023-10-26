from hashlib import sha256
from django.shortcuts import render
from .models import User, Birds, ViewedUser

"""
Основные функции:
auth - процесс аутентфикации пользователя.


"""


def auth(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        pswHash = sha256(password.encode('utf-8')).hexdigest()
        SQLdata = User.objects.raw(f"SELECT login, password FROM User WHERE login = {login} AND password = {pswHash}")
        if SQLdata is True:  # Если логин и пароль существуют, то переходим на основную форму, это процесс авторизации.
            return render(request, 'viewBirds.html', {"login": login})
        elif login is not None:
            ErorrMessage = "Incorrect username or password."
            return render(request, 'auth.html', {"Error": ErorrMessage})
    return render(request, 'auth.html')



#def userView(request):


def viewBirds(request):
    birds = Birds.objects.all()
    return render(request, 'viewBirds.html', {"birds": birds})


def creatBirds(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        PNG = request.POST.get('PNG')
