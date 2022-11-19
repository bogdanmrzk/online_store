from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/photos')
    upload_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=False, default=1, db_index=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category





