from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('index/', views.ItemList, name='index'),
  path('add/', views.ItemCreate.as_view(), name='item_create'),
  path('index/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]