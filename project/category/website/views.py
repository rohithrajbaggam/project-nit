from rest_framework import generics, status, pagination
from rest_framework.response import Response
from category.models import CateogryModel, BrandModel
from .serializers import CateoryModelSerializer, BrandModelSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = CateogryModel.objects.all()
    serializer_class = CateoryModelSerializer
    pagination_class = pagination.LimitOffsetPagination


class BrandListAPIView(generics.ListAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    pagination_class = pagination.LimitOffsetPagination 
