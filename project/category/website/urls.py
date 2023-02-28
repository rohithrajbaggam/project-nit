from django.urls import path 
from .views import CategoryListAPIView, BrandListAPIView

urlpatterns = [
    path("cateogry-list-api/", CategoryListAPIView.as_view(), name="CategoryListAPIView"),
    path("brand-list-api/", BrandListAPIView.as_view(), name="BrandListAPIView"),
]


