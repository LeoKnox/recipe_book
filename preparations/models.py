from django.db import models

class Preparation(models.Model):
    prep = models.CharField(max_length=50)
    directions = models.TextField()
    tools = models.CharField(max_length=100)

class Recipe_Prep(models.Model):
    prep_name = models.CharField(max_length=50)
    recipe_id = models.IntegerField()

def __str__(self):
    return self.title