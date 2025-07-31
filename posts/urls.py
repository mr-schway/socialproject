from django.urls import path
from posts import views

urlpatterns = [
  # path('', views.index, name='index'),
  path('create/', views.post_create, name='post_create'),
]