from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('update/<int:pk>/', views.update, name="update"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_view, name='logout'),
]