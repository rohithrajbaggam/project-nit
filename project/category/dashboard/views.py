from rest_framework import generics, pagination, status
from rest_framework.response import Response
from category.models import CateogryModel, BrandModel
from .serializer import CateoryModelSerializer, BrandModelSerializer

# creating and listing categories 
class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = CateogryModel.objects.all()
    serializer_class = CateoryModelSerializer
    pagination_class = pagination.LimitOffsetPagination

# Update/deleting a cateogry
class CategoryGenericAPIView(generics.GenericAPIView):
    # get, Put, Delete 
    queryset = CateogryModel.objects.all()
    serializer_class = CateoryModelSerializer

    def get(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data, instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data is Updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        queryset.delete()
        Response({"message" : "Item is deleted"}, status=status.HTTP_200_OK)


# Brand List/Create 
class BrandModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    pagination_class = pagination.LimitOffsetPagination


# Brand Update/Delete 
class BrandModelGenericAPIView(generics.GenericAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer

    def get(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data, instance=queryset)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Data is Updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = self.queryset.filter(pk=id).last()
        if not queryset:
            return Response({"message" : "Product with this id doesn't exists"}, status==status.HTTP_400_BAD_REQUEST)
        queryset.delete()
        Response({"message" : "Item is deleted"}, status=status.HTTP_200_OK)
