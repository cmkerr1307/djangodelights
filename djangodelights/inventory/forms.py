from django import forms
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases

class MenuCreateForm(forms.modelForm):
    class Meta:
        model = MenuItems
        fields = "__all__"
