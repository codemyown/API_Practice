from django.shortcuts import render
from django.http import JsonResponse
from .models import City,Student
from .serializers import StudentSerializers,CitySerializers,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User





# Create your views here.

class UserViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class StudentListView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    

class StudentListViewByID(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    

class CitySerializerView(generics.ListAPIView,generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers
    


class CitySerializerViewById(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers