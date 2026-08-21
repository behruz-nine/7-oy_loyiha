from django.urls import path
from . import views

urlpatterns = [path('create_product/', views.CreateProduct.as_view()),
               path('list_product/', views.ListProduct.as_view()),
               path('product/<int:product_id>/', views.DetailProduct.as_view()),
               path('put_product/<int:product_id>/', views.PutProduct.as_view()),
               path('patch_product/<int:product_id>/', views.PatchProduct.as_view()),
               path('delete_product/<int:product_id>/', views.DeleteProduct.as_view())]