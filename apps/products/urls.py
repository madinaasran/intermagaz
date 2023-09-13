from django.urls import path
from apps.products.views import ProductAPIView, ProductDetailAPIView, LikeAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='product-list'),
    path('product/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    path('likes', LikeAPIView.as_view(), name='likes')
]
