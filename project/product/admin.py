from django.contrib import admin
from .models import ProductImageModel, ProductModel, ProductReviewImageModel, ProductReviewModel
# Register your models here.

admin.site.register(ProductImageModel)
admin.site.register(ProductModel)
admin.site.register(ProductReviewImageModel)
admin.site.register(ProductReviewModel)

