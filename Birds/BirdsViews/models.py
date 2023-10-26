from django.db import models
"""
Имеется 3 модели:
Birds - птицы;
ViewedUser- просмотренные птицы пользователям;
User - пользователи.
"""


class Birds(models.Model):
    id_birds = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    PNG = models.ImageField(upload_to='images')
    feather_color = models.TextField(max_length=70, null=False)


class ViewedUser(models.Model):
    id_view = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_birds = models.ForeignKey('Birds', on_delete=models.PROTECT, null=False, unique=True)
    id_user = models.ForeignKey('User', on_delete=models.PROTECT, null=False)
    DataTime = models.DateTimeField(null=False)


class User(models.Model):
    id_user = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=100, null=False)
    login = models.CharField(max_length=50, null=False, unique=True)
    mail = models.EmailField(null=True)
    password = models.CharField(max_length=100, null=False)


def __str__(self):
    return self.name, self.PNG, self.feather_color, self.id_birds