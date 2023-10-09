from django.urls import path
from .import views


urlpatterns = [
    path('',views.ec.as_view(),name='ec'),
    path('eg',views.eg.as_view(),name='eg'),
    path('er/<int:pk>/',views.er.as_view(),name='er'),
    path('eu/<int:pk>/',views.eu.as_view(),name='eu'),
    path('ed/<int:pk>/',views.ed.as_view(),name='ed'),
]
