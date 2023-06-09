from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('account/signup/', views.signup, name='signup'),
    path('account/profile/<int:pk>/', views.profile, name='profile'),
    path('account/profile/<int:pk>/update/', views.update_profile, name='update-profile'),


    path('employee/create/', views.employee_create, name='emp-create'),
    path('employee/list/', views.employee_list, name='emp-read'),
    path('employee/search/', views.employee_search, name='emp-search'),
    path('employee/update/<int:id>/', views.employee_update, name='emp-update'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp-delete'),

    path('product/create/', views.product_create, name='prod-create'),
    path('product/list/', views.product_list, name='prod-read'),
    path('product/search/', views.product_search, name='prod-search'),
    path('product/update/<int:id>/', views.product_update, name='prod-update'),
    path('product/delete/<int:id>/', views.product_delete, name='prod-delete'),
]