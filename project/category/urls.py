from django.urls import path, include 

urlpatterns = [
    path("dashboard/", include("category.dashboard.urls")),
    path("website/", include("category.website.urls")),
]
