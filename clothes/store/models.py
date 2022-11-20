from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/photos')
    upload_time = models.DateTimeField(auto_now=True)
    category_name = models.ForeignKey("Category", on_delete=models.CASCADE, null=False, default='Another category')

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("category_v", kwargs={"category_name": self.category})

    def __str__(self):
        return self.category





