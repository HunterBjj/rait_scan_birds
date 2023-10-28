from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.auth, name='auth'),
    path('viewBirds.html/', views.viewBirds, name='viewBirds'),
    path('creatBirds.html/', views.creatBirds, name='creatBirds'),
    path('creatUser.html/', views.rgstrUser, name='rgstrUser'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)