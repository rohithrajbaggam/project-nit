from .serializer import ProductSerializer, ProductImageModelSerializer
from product.models import ProductModel, ProductImageModel
from rest_framework import generics, status, pagination
from rest_framework.response import Response


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.LimitOffsetPagination

class ProductImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImageModel.objects.all()
    serializer_class = ProductImageModelSerializer
    pagination_class = pagination.LimitOffsetPagination 

    def get_queryset(self):
        product_queryset = ProductModel.objects.get(pk=self.kwargs["product_id"])
        return product_queryset.image.all()
    
    def create(self, request, product_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            product_image_instance = ProductImageModel.objects.create(
                image=request.data["image"]
            )
            product_queryset = ProductModel.objects.get(pk=product_id)
            product_queryset.image.add(product_image_instance.pk)
            product_queryset.save()
            return Response({"message" : "Data is inserted"})
        else:
            return Response(serializer.errors)
        return Response("ok")

