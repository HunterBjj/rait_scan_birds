from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('viewBirds.html', views.viewBirds),
]