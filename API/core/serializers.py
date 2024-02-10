from rest_framework import serializers
from .models import Student,City
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password"]
        

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        

class CitySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = "__all__"
    