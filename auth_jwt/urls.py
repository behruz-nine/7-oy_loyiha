from django.urls import path
from . import views

urlpatterns = [path('auth3/', views.SignUpView3.as_view()),
               path('login3/', views.LoginView3.as_view()),
               path('profile3/', views.Profile3.as_view()),
               path('get_accesstoken/', views.TokenRefresh.as_view()),
               path('change_password3/', views.PasswordChangeView3.as_view())]