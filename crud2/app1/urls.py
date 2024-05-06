from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_page, name='cars_page'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('book/new/', views.car_create, name='car_create'),
    path('book/<int:pk>/edit/', views.car_update, name='car_update'),
    path('book/<int:pk>/delete/', views.car_delete, name='car_delete'),
]
