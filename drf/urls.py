from django.urls import path
from . import views

urlpatterns = [path('create-get/', views.create_get_product),
               #path('get/', views.getproducts),
               path('product_dppd/<int:product_id>/', views.product_dppd),
               #path('put/<int:product_id>/', views.put_product),
               #path('patch/<int:product_id>/', views.patch_product),
               #path('delete/<int:product_id>/', views.delete_product)
               ]

