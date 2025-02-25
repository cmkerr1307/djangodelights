from django.shortcuts import render
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    context = {"name": username}
    return render(request, "inventory/home.html", context)

class IngredientList(ListView):
    model = Ingredients
    template_name = "inventory/ingredient_list.html"

class IngredientCreate(CreateView):
    model = Ingredients
    template_name = "inventory/ingredient_create_form.html"
    fields = ["name", "quantity", "unit", "unit_price"]

class IngredientUpdate(UpdateView):
    model = Ingredients
    template_name = "inventory/ingredient_update_form.html"
    fields = ["name", "quantity", "unit", "unit_price"]

class IngredientDelete(DeleteView):
    model = Ingredients
    template_name = "inventory/ingredient_delete_form"
    



class MenuList(ListView):
    model = MenuItems
    template_name = "inventory/menu_list.html"

class MenuCreate(CreateView):
    model = MenuItems
    template_name = "inventory/menuItem_create_form.html"
    fields = ["title", "price"]

class MenuUpdate(UpdateView):
    model = MenuItems
    template_name = "inventory/menuItem_update_form.html"
    fields = ["title", "price"]

class MenuDelete(DeleteView):
    model = MenuItems
    template_name = "inventory/menuItem_delete_form.html"



class RecipeCreate(CreateView):
    model = RecipeRequirements
    template_name = "inventory/recipe_create_form.html"
    fields = ["menu_item", "ingredient", "quantity"]

class RecipeUpdate(UpdateView):
    model = RecipeRequirements
    template_name = "inventory/recipe_update_form.html"
    fields = ["menu_item", "ingredient", "quantity"]

class RecipeDelete(DeleteView):
    model = RecipeRequirements
    template_name = "inventory/recipe_delete_form.html"



class PurchaseList(ListView):
    model = Purchases
    template_name = "inventory/purchase_list.html"

class PurchaseCreate(CreateView):
    model = Purchases
    template_name = "inventory/purchase_create_form.html"
    fields = ["menu_item", "timestamp"]

class PurchaseUpdate(UpdateView):
    model = Purchases
    template_name = "inventory/purchase_update_form.html"
    fields = ["menu_item", "timestamp"]

class PurchaseDelete(DeleteView):
    model = Purchases
    template_name = "inventory/purchase_delete_form.html"


class Financial():
    revenue = 0
    cost = 0