from rest_framework import generics, status, pagination
from rest_framework.response import Response
from category.models import CateogryModel
from .serializers import CateoryModelSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = CateogryModel.objects.all()
    serializer_class = CateoryModelSerializer
    pagination_class = pagination.LimitOffsetPagination



