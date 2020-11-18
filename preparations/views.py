from django.shortcuts import render, HttpResponse

from .models import Preparation
from recipes.models import Recipe

def index(request):
    prep_data = Preparation.objects.values()
    recipe_data = Recipe.objects.values()
    context = {'prep_data': prep_data, 'recipe_data': recipe_data}
    return render(request, 'preparations/index.html', context)