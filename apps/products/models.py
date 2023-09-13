from django.db import models
from apps.categories.models import Category
from apps.users.models import User


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    country = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_product')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_like')

    def __str__(self):
        return f"{self.user} - {self.product}"
