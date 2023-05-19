
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('conocenos/', views.conocenos, name = 'conocenos'),
    path('servicios/', views.servicios, name = 'servicios'),
    path('contacto/', views.enDesarrollo, name = 'enDesarrollo'),
]
