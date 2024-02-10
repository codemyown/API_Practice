from django.urls import path
from .views import  UserViewList, StudentListView,CitySerializerView,StudentListViewByID,CitySerializerViewById


urlpatterns = [
    path("",UserViewList.as_view()),
    path("api/student",StudentListView.as_view()),
    path("api/student/update/<int:pk>",StudentListViewByID.as_view()),
    path("api/city",CitySerializerView.as_view()),
    path("api/city/update/<int:pk>",CitySerializerViewById.as_view())
    
]
