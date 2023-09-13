from rest_framework import serializers
from apps.categories.models import Category
from apps.products.models import Product, Like


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'quantity', 'price', 'country', 'created_at', 'category', 'owner',]


class ProductUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150, required=False)
    description = serializers.CharField(max_length=10000, required=False)
    image = serializers.ImageField(use_url=True, allow_empty_file=True, required=False)
    quantity = serializers.IntegerField(required=False)
    price = serializers.IntegerField(required=False)
    country = serializers.CharField(max_length=50, required=False)
    created_at = serializers.CharField(max_length=20, required=False)
    category = serializers.PrimaryKeyRelatedField(required=False, queryset=Category.objects.all())

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.country = validated_data.get('country', instance.country)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

