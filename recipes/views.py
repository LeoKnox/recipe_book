from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from recipes.forms import RecipeForm

from .models import Recipe

def index(request):
    recipes_list = Recipe.objects.values()
    template = loader.get_template('recipes/index.html')
    context = {
        'recipes_list': recipes_list,
    }
    return render(request, 'recipes/index.html', context)

def create(request):
    context = {}
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    context['form'] = form
    return render(request, 'recipes/create.html', context)

def edit(request, recipe_id):
    edit_room = RecipeForm(request.POST or None)
    if edit_room.is_valid():
        update = Recipe.objects.get(id = recipe_id)
        update.name = request.POST.get('name')
        update.ingredients = request.POST.get('ingredients')
        update.directions = request.POST.get('directions')
        update.cook_time = request.POST.get('cook_time')
        update.save()
        return redirect('/index/')
    recipe = Recipe.objects.get(id = recipe_id)
    recipe_data = {
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'directions': recipe.directions,
        'cook_time': recipe.cook_time
    }
    form = RecipeForm(initial=recipe_data)
    return render(request, 'recipes/edit.html', {'form': form})

def detail(request, recipe_id):
    return render(request, 'recipes/detail.html', {})

def delete(request, recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('/index/')