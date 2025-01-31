from django.db import models

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length = 10)
    unit_price = models.IntegerField(default=0)

class MenuItems(models.Model):
    title = models.CharField(max_length = 30)
    price = models.IntegerField(default=0)

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    timestamp = models.DateTimeField