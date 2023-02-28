from .views import CategoryCreateListAPIView, CategoryGenericAPIView, BrandModelListCreateAPIView, BrandModelGenericAPIView
from django.urls import path 

urlpatterns = [
    path("category-list-create-api/", CategoryCreateListAPIView.as_view(), name="CategoryCreateListAPIView"),
    path("category-list-create-api/<id>/", CategoryGenericAPIView.as_view(), name="CategoryGenericAPIView"),

    path("brand-list-create-apiview/", BrandModelListCreateAPIView.as_view(), name="BrandModelListCreateAPIView"),
    path("brand-list-create-apiview/<id>/", BrandModelGenericAPIView.as_view(), name="BrandModelGenericAPIView"),
   
]

