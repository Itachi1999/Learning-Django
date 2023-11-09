from django.db import models

# Create your models here.
class Book(models.Model):
    # Django models already has a autoincrementing ID field
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()

        
    
