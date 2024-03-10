from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 50)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default="",null=False)
    
    def __str__(self):
        return f"{self.title} {self.rating}"
    
    def get_absolute_path(self):
        return reverse("book-detail",args=[self.slug])
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)