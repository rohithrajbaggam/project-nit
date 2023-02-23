from django.db import models
from product.models import ProductModel
from django.contrib.auth import get_user_model
# Create your models here.

class UserOrderModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserOrderModel_user")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="UserOrderModel_product")

    quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=7, decimal_places=2 )
    # shoe -> 1500 -> Q - 2 -> 1500*2=3000
    total_price = models.DecimalField(max_digits=7, decimal_places=2 )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





