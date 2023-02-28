from django.urls import path, include 

urlpatterns = [
    path("website/", include("wishlist.website.urls")),
    path("dashboard/", include("wishlist.dashboard.urls")),
]


