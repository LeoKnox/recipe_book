from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

        fields = [
            'name',
            'categories',
            'ingredients',
            'directions',
            'cook_time',
        ]
        labels = {
            'cook_time': 'Cook Time(in minutes)'
        }