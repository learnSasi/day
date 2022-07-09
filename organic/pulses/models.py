from django.db import models

# Create your models here.
class vendor(models.Model):
    name=models.FileField(max_length=100)
    mobile_no=models.FileField(max_length=100)
    product_name=models.FileField(max_length=100)
    location=models.FileField(max_length=100)
    password=models.FileField(max_length=100)
    re_password=models.FileField(max_length=100)


class snacks(models.Model):
    product_image= models.FileField()
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    health_benefits= models.TextField()