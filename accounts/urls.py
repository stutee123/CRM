from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('createorder/', views.createOrder, name='create_order'),
    path('updateorder/<str:pk>/', views.updateOrder, name='update_order'),
    path('deleteorder/<str:pk>/', views.deleteOrder, name='delete_order'),
    
    
]
