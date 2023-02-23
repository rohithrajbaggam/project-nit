from django.db import models
from django.contrib.auth import get_user_model
from .utils import GenderEnumType
# Create your models here.

class UserAddressModel(models.Model):
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)


class UserProfileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="UserProfileModel_user")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="media/images/")
    gender = models.CharField(max_length=100, choices=GenderEnumType.choices())
    address = models.ManyToManyField(UserAddressModel, related_name="UserProfileModel_address", blank=True)
    # male, female, others

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




