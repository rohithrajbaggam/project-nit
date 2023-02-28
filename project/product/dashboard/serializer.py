from product.models import ProductModel, ProductImageModel
from rest_framework import serializers
from category.models import CateogryModel, BrandModel

class ProductImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = "__all__"


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = "__all__"

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CateogryModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_detail = serializers.SerializerMethodField()
    brand_details = serializers.SerializerMethodField()
    product_images = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = "__all__"

    def get_product_images(self, obj=ProductModel):
        try:
            data = ProductImageModelSerializer(obj.image.all(), many=True).data 
            # print(obj.image.all())
        except:
            data = {}
        return data

    def get_category_detail(self, obj=ProductModel):
        try:
            data = CategoryModelSerializer(obj.category, many=False).data 
            return data 
        except Exception as e:
            data = {}
        return data 
    
    def get_brand_details(self, obj=BrandModel):
        try:
            data = BrandModelSerializer(obj.brand, many=False).data 
            return data 
        except Exception as e:
            data = {}
        return data 
        
