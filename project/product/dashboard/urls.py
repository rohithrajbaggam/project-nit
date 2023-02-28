from django.urls import path 
from .views import ProductListCreateAPIView , ProductImageListCreateAPIView

urlpatterns = [
    path("product-list-create-api/", ProductListCreateAPIView.as_view(), name="ProductListCreateAPIView"),
    path("product-image-create-list-api/<product_id>/", ProductImageListCreateAPIView.as_view(), name="ProductImageListCreateAPIView")
]
