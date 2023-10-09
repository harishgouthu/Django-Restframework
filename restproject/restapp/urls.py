from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('updt/<int:id>/',views.updt,name='updt'),
    path('dlt/<int:id>/',views.dlt,name='dlt'),
]