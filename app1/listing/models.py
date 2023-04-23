from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Type (models.Model):
    name = models.fields.CharField(max_length=100)


class Product (models.Model):
    name = models.fields.CharField(max_length=100)
    category = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    #category = models.fields.CharField(max_length=25)
    date_in = models.fields.IntegerField(default=2023, validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    status = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
