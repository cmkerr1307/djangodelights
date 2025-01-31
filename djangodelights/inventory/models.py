from django.db import models

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length = 10)
    unit_price = models.IntegerField(default=0)

class MenuItems(models.Model):
    pass

class RecipeRequirements(models.Model):
    pass

class Purchases(models.Model):
    pass