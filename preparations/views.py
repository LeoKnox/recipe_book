from django.shortcuts import render, HttpResponse

from .models import Preparation, Recipe_Prep
from recipes.models import Recipe

def index(request):
    prep_data = Preparation.objects.values()
    recipe_data = Recipe.objects.values()
    recipe_prep = Recipe_Prep.objects.get(recipe_id=1)
    print(recipe_prep.prep_name)
    context = {'prep_data': prep_data, 'recipe_data': recipe_data, 'recipe_prep': recipe_prep}
    return render(request, 'preparations/index.html', context)