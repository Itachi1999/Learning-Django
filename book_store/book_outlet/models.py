from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    # Django models already has a autoincrementing ID field
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    is_bestselling = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} by {self.author} rated {self.rating}"

        
    
