from rest_framework import serializers
from .models import *

class EmpSerializer(serializers.ModelSerializer):
      class Meta:
            model = employee
            fields='__all__'
