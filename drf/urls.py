from django.urls import path
from . import views

urlpatterns = [path('create/', views.create_product),
               path('get/', views.getproducts),
               path('detail/<int:product_id>/', views.product_details),
               path('put/<int:product_id>/', views.put_product),
               path('patch/<int:product_id>/', views.patch_product),
               path('delete/<int:product_id>/', views.delete_product)]

