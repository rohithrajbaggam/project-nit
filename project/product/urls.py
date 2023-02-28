from django.urls import path, include 
urlpatterns = [
    path("dashboard/", include("product.dashboard.urls")),
]


