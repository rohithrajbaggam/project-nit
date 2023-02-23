from .views import TestAPIView
from django.urls import path 

urlpatterns = [
    path("test-api/", TestAPIView.as_view(), name="TestAPIView"),
]

