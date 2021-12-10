from rest_framework import serializers
from .models import clientmst
from .models import Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientmst
        fields = '__all__'


class projectSerializer(serializers.ModelSerializer):
     class Meta:
         model = Project
         fields = '__all__'     