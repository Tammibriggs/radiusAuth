from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_n_login, name="access"),
    path('profile/', views.profile, name="profile")
]