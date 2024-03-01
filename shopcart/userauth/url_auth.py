from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_page),
    path('login/', views.login_page),
    path ('logout/', views.logout_page ),
    path ('forget_password/', views.forget_password),
    path('change_password/', views.change_password, name='change-password')
]