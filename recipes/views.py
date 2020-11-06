from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Recipe

def index(request):
    recipes_list = Recipe.objects.values()
    template = loader.get_template('recipes/index.html')
    context = {
        'recipes_list': recipes_list,
    }
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    return HttpResponse("yo %s" % recipe_id)