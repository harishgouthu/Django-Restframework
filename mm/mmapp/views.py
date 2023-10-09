from django.shortcuts import render 
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
# Create your views here.
class eg(ListAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class ec(CreateAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class er(RetrieveAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class eu(UpdateAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class ed(DestroyAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class egc(ListCreateAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class eru(RetrieveUpdateAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class erd(RetrieveDestroyAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
class erud(RetrieveUpdateDestroyAPIView):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      
      
     
      


