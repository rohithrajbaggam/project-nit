from rest_framework import serializers
from category.models import CateogryModel, BrandModel


class CateoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CateogryModel
        fields = "__all__"


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = "__all__"
