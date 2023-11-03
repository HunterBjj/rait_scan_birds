from hashlib import sha256
from django.shortcuts import render
from .models import User, Birds, ViewedUser
import datetime

"""
Наименование функции используется camel Case.
Все 5 функций возвращают render с переданными аргументами.
Для хеширования пароля пользователя используется sha256.
Логин передается в качестве доказательство авторизации, а также для вывода
списка просмотров птиц авторизированным пользователям.
"""


def auth(request):
    """Процесс аутентификации пользователя."""
    if request.method == 'POST':
        login = request.POST.get("login")
        password = request.POST.get("password")
        pswHash = sha256(password.encode('utf-8')).hexdigest()
        user = User.objects.filter(login=login, password=pswHash)

        if user:  # Если логин и пароль существуют, то переходим на основную форму, это процесс авторизации.
            return render(request, 'viewBirds.html/', {"login": login})
        elif login is not None:
            ErorrMessage = "Incorrect username or password."
            return render(request, 'auth.html/', {"Error": ErorrMessage})

    return render(request, 'auth.html/')


def viewUser(request):
    """Вывод просмотренных птиц пользователям."""
    login = request.POST.get("login")  # FIXME Не стоит передавать значение от пользователя в сырой SQL-запрос.
    sql_get = """SELECT Birds.name, Birds.PNG, Birds.feather_color, ViewedUser.DataTime
                                  FROM User, Birds, ViewedBirds
                                  WHERE User.login = %s
                                  AND Birds.id_birds = ViewedBirds.id_birds
                                  AND User.id_user = ViewedBirds.id_user
                                  GROUP BY ViewedBirds.DataTime;""" % login
    view = ViewedUser.objects.raw(sql_get)  # FIXME может привести к SQL-инъекциям.

    return render(request, 'viewUser.html/', {'view': view}, {'login': login})


def rgstrUser(request):
    """Регистрация пользователя."""
    if request.method == 'POST':
        user = User()
        user.login = request.POST.get('login')
        user.full_name = request.POST.get('full_name')
        password = request.POST.get('password')
        user.password = sha256(password.encode('utf-8')).hexdigest()  # Сохраняем пароль в виде хеша.
        user.mail = request.POST.get('email')
        user.save()
        return render(request, 'auth.html/')

    return render(request, 'createUser.html/')


def viewBirds(request):
    """Вывод птиц."""
    login = request.POST.get('login')
    birds = Birds.objects.all()
    if request.GET.get('save'):  # Сохраняем выбранную птицу в избранные.
        view_bird = ViewedUser()
        view_bird.id_birds = request.POST.get('id_birds')
        view_bird.id_user = User.objects.filter(id_user=login).values("id_user")
        view_bird.DataTime = datetime.datetime.now()
        view_bird.save()
        return render(request, 'viewBirds.html/', {"birds": birds})

    return render(request, 'viewBirds.html/', {"birds": birds})


def creatBirds(request):
    """Создание птиц."""
    if request.method == 'POST':
        birds = Birds()
        birds.name = request.POST.get('name')
        birds.feather_color = request.POST.get('color')
        birds.PNG = request.POST.get('PNG')
        birds.save()
        return render(request, 'createBirds.html/')

    return render(request, 'createBirds.html/')
