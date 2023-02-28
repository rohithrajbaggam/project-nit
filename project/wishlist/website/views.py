from .serializers import UserWishListModelSerializer
from wishlist.models import UserWishlistModel
from rest_framework import generics, permissions, authentication, status 
from rest_framework.response import Response

class UserWishListModelGenericAPIView(generics.ListCreateAPIView):
    queryset = UserWishlistModel.objects.all()
    serializer_class = UserWishListModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication, authentication.BaseAuthentication, authentication.SessionAuthentication]
    # authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        # print(self.request.user)
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data, context={"request" : request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    




