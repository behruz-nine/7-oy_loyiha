from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.CreateProductViewSet, basename='create_product' )
router.register(r'product_list', views.ListProductViewSet, basename='products')
router.register(r'product_detail', views.DetailProductViewSet, basename='product_detail')
router.register(r'put_product', views.PutProductViewSet, basename='put_product')
router.register(r'patch_product', views.PatchProductViewSet, basename='patch_product')
router.register(r'delete_product', views.DestroyProductViewSet, basename='delete_product')
urlpatterns = router.urls