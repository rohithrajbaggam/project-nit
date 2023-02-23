from django.db import models
from category.models import CateogryModel, BrandModel
from django.contrib.auth import get_user_model
# Create your models here.
class ProductImageModel(models.Model):
    image = models.FileField(upload_to="media/products/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1, 2, 3

class ProductModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    actual_price = models.DecimalField(max_digits=7, decimal_places=2 )
    current_price = models.DecimalField(max_digits=7, decimal_places=2 )
    discount_price = models.DecimalField(max_digits=7, decimal_places=2 )
    # 100 -> 10% => 100-10 -> 90
    percentage = models.IntegerField()
    image = models.ManyToManyField(ProductImageModel, related_name="ProductModel_image", blank=True)
    category = models.ForeignKey(CateogryModel, on_delete=models.CASCADE, related_name="ProductModel_category")
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="ProductModel_brand")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductReviewImageModel(models.Model):
    image = models.FileField(upload_to="media/products/reviews/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductReviewModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="ProductReviewModel_user")
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(ProductReviewImageModel, blank=True, related_name="ProductReviewModel_image")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




