from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from apps.products.models import Product, Like
from apps.products.serializers import ProductSerializer, ProductUpdateSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save(owner=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, pk, *args, **kwargs):
        try:
            user = request.user
            data = request.data
            product = Product.objects.filter(id=pk, owner=user).first()
            if product:
                serializer = ProductUpdateSerializer(data=data, partial=True)
                if serializer.is_valid():
                    serializer.update(product, serializer.validated_data)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Product not found!"})
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, *args, **kwargs):
        try:
            user = request.user
            product = Product.objects.filter(id=pk, owner=user).first()
            if product:
                product.delete()
                return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Product not found!"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


class LikeAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

def get(self, request):
        user = request.user
def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data['product']
        product = Product.objects.get(id=product_id)

        like_obj = Like.objects.filter(product=product, user=user).first()
        if like_obj:
            like_obj.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        else:
            like = Like.objects.create(user=user, product=product)
            return Response({"message": "Created"}, status=status.HTTP_201_CREATED)