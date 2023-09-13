
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from apps.users.serializers import UserSerializer, UserCreateSerializer


class RegisterAPIView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    authentication_classes = (JWTAuthentication, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
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