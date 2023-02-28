from django.urls import path, include 

urlpatterns = [
    path("website/", include("users.website.urls")),
]
