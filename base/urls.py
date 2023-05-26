from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('employee/create/', views.employee_create, name='emp-create'),
    path('employee/list/', views.employee_list, name='emp-read'),
    path('employee/search/', views.employee_search, name='emp-search'),
    path('employee/update/<int:id>/', views.employee_update, name='emp-update'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp-delete'),
]