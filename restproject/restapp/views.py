from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):   
       emp_obj= employee.objects.all()
       serializer=EmpSerializer(emp_obj,many=True)
       return Response(serializer.data)
@api_view(['POST'])
def create(request):
       emp_obj=employee.objects.all()
       serializer=EmpSerializer(data=request.data)
       if serializer.is_valid():
              serializer.save()
       return Response(serializer.data)
@api_view(['POST'])
def updt(request,id):   
       emp_obj= employee.objects.get(id=id)
       serializer=EmpSerializer(instance=emp_obj,data=request.data)
       if serializer.is_valid():
              serializer.save()
@api_view(['DELETE'])
def dlt(request,id):   
       emp_obj= employee.objects.get(id=id)
       emp_obj.delete()
       return Response('successfully deleted')
       

