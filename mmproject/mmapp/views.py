from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.
class ec(GenericAPIView,CreateModelMixin):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      def post(self,request):
            return self.create(request)
            return redirect('eg')
class eg(GenericAPIView,ListModelMixin):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      def get(self,request):
            return self.list(request)
class er(GenericAPIView,RetrieveModelMixin):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      def get(self,request,**kwargs):
            return self.retrieve(request,**kwargs)
class eu(GenericAPIView,UpdateModelMixin):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      def put(self, request, **kwargs):
            return self.update(request,**kwargs)
class ed(GenericAPIView,DestroyModelMixin):
      queryset=employee.objects.all()
      serializer_class=EmpSerializer
      def delete(self, request, **kwargs):
            return self.destroy(request,**kwargs)