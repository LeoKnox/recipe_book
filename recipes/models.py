from django.db import models

CATEGORIES = [
    ('Food', 'food'),
    ('Other Stuff'),
]

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=25, choices='CATEGORIES')
    ingredients = models.TextField()
    directions = models.TextField()
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name