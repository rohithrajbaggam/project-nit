from .serializers import UserWishListModelSerializer
from wishlist.models import UserWishlistModel
from rest_framework import generics, permissions, authentication, status, filters
from rest_framework.response import Response


class UserWishListModelGenericAPIView(generics.ListAPIView):
    queryset = UserWishlistModel.objects.all()
    serializer_class = UserWishListModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    