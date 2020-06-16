from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('students/', views.student_list, name='students'),
    path('ptdetails/<int:pk>', views.newone, name='details'),
    path('filter/', views.search_api, name='filter'),
    path('classview/', views.UserListView.as_view())
]
