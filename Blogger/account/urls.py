from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name = "logout_page")
]