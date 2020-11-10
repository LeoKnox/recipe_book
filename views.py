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

def detail(request, recipe_id):
    return HttpResponse("yo %s" % recipe_id)

def delete(request, recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('/index')