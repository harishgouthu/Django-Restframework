from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.eg.as_view(),name='eg'),
    path('ec',views.ec.as_view(),name='ec'),
    path('er/<int:pk>/',views.er.as_view(),name='er'),
    path('eu/<int:pk>/',views.eu.as_view(),name='eu'),
    path('ed/<int:pk>/',views.ed.as_view(),name='ed'),
    path('egc',views.egc.as_view(),name='egc'),
    path('eru/<int:pk>/',views.eru.as_view(),name='eru'),
    path('erd/<int:pk>/',views.erd.as_view(),name='erd'),
    path('erud/<int:pk>/',views.erud.as_view(),name='erud'),
    


]
