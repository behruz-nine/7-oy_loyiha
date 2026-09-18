from django.urls import path
from . import views

urlpatterns = [path('create_auth2/', views.SignUpView2.as_view()),
               path('login_auth2/', views.LoginView2.as_view()),
               path('profile2/', views.ProfileView2.as_view()),
               path('update_profile2/', views.ProfileUpdateView2.as_view()),
               path('change_password2/', views.PasswordChangeView2.as_view())]