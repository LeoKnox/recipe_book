from django.shortcuts import render, HttpResponse
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
    recipe = Recipeform(request.POST or None)
    return render(request, 'recipes/create.html', {})

def detail(request, recipe_id):
    return HttpResponse("yo %s" % recipe_id)