from django.urls import path 
from .views import UserWishListModelGenericAPIView 

urlpatterns = [
    path("wishlist-list/", UserWishListModelGenericAPIView.as_view(), name="UserWishListModelGenericAPIView")
]


