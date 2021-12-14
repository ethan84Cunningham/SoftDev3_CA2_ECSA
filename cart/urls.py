from os import name
from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add/<uuid:film_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<uuid:film_id>/', views.cart_remove, name='cart_remove'),   
    path('full_remove/<uuid:film_id>/', views.full_remove, name='full_remove'),
]