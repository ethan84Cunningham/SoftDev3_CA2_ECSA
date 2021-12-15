from django.urls import path
from shop import views
from .views import signinView, signupView, signoutView

urlpatterns = [
    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signoutView, name='signout'),
] 