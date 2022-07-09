from django.db import models

# Create your models here.
class ppl(models.Model):
    name=models.FileField(max_length=100)
    mobile_no=models.FileField(max_length=100)
    gender=models.FileField(max_length=100)
    password=models.FileField(max_length=100)
    re_password=models.FileField(max_length=100)

class review(models.Model):
    star =models.CharField(max_length=100)
    review =models.CharField(max_length=1000)
    suma =models.CharField(max_length=1000)


