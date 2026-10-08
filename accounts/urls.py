from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name = "accounts/login.html"), name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path('forget-password/',views.forget_password,name='forget_password')
]
