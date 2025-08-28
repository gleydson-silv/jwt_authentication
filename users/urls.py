from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('forgot_password/', views.forgot_password),
    path('reset_password/', views.reset_password),
    path('reset_password/<uidb64>/<token>/', views.reset_password)
    ]
