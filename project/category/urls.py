from django.urls import path, include 

urlpatterns = [
    path("dashboard/", include("category.dashboard.urls")),
]
