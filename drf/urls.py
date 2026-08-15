from django.urls import path
from . import views

urlpatterns = [path('create/', views.create_product),
               path('get/', views.getproducts),
               path('detail/<int:product_id>/', views.product_details)]

