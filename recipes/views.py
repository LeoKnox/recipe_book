from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Recipe

def index(request):
    recipes_list = Recipe.objects.value()
    template = loader.get_template('recipes/index.html')
    context = {
        'recipes_list': recipes_list,
    }
    return HttpResponse(template.render(context, request))