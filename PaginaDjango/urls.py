
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('registerProduct/', views.registerProducts, name='registerProducts'),
    path('registerClient/', views.registerClient, name='registerClient'),
    path('registerCustommer/', views.registerCustommer, name='registerCustommer'),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('registerUser/', views.registerUser, name="registerUser"),
    path('admin/', admin.site.urls),
]
