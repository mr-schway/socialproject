from django.urls import path

from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/', views.user_login, name='login'),
  # path('logout/', auth_views.LogoutView.as_view()), # django 4
  path("logout/", auth_views.LogoutView.as_view(http_method_names=["post", "get", "options"],template_name='users/logout.html'), name='logout'),
]