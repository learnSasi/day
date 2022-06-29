from django.db import models

# Create your models here.
class first_image(models.Model):
    Name = models.CharField(max_length=100)
    Photo = models.FileField()
    Book = models.FileField()
    Clip = models.FileField()