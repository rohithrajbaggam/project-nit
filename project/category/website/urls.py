from django.urls import path 
from .views import CategoryListAPIView

urlpatterns = [
    path("cateogry-list-api/", CategoryListAPIView.as_view(), name="CategoryListAPIView"),
]


