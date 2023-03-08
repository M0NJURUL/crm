from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registrationPage, name="registration"),
    path('login/', views.loginPage, name="registration"),
    


    path('', views.home, name = 'home'),
    path('product/', views.product, name = 'product'),
    path('customer/<str:pk>/', views.customer, name = 'customer'),

    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]

#<a class="btn btn-primary  btn-sm btn-block" href="{% url 'create_order' %}">Create Order</a>
#url routing is awesome