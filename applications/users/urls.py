from django.contrib import admin
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'registro/', 
        views.UserRegisterView.as_view(),
        name='registro'
    ),
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='login'
    ),
    path(
        'logout', 
        views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'update', 
        views.UpdatePasswordView.as_view(),  
        name='update'
    ),
    path(
        'error', 
        views.ErrorView.as_view(), 
        name='error'
    ),
    path(
        'verificacion/<id>/', 
        views.CodeVerificationView.as_view(), 
        name='verificacion'
    )
]