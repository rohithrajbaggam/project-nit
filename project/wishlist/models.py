from django.db import models
from product.models import ProductModel
from django.contrib.auth import get_user_model
# Create your models here.

class UserWishlistModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserWishlistModel_user")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="UserWishlistModel_product")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


