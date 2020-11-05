from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    directions = models.TextField()
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name