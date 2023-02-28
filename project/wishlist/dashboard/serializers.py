from rest_framework import serializers
from wishlist.models import UserWishlistModel


class UserWishListModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserWishlistModel
        fields = "__all__"

    