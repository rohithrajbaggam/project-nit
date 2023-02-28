from django.urls import path 
from .views import UserWishListModelGenericAPIView

urlpatterns = [
    path("my-wishlist/", UserWishListModelGenericAPIView.as_view(), name="UserWishListModelGenericAPIView"),
]


