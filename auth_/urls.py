from django.urls import path
from . import views
urlpatterns = [path('create_auth/', views.SignUpView.as_view()),
               path('login/', views.LoginView.as_view()),
               path('profile/', views.ProfileView.as_view()),
               path('profile_update/', views.ProfileUpdateView.as_view()),
               path('password_change/', views.PasswordChangeView.as_view())]