from rest_framework import serializers
from wishlist.models import UserWishlistModel


class UserWishListModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = UserWishlistModel
        fields = "__all__"

    def validate(self, data):
        if UserWishlistModel.objects.filter(user=self.context["request"].user, product=data["product"]).exists():
            raise serializers.ValidationError({
                "message" : "Product is Already Added to the wishlist"
            })
        return data 