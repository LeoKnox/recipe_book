from django.db import models

class Preparation(models.Model):
    prep = models.CharField(max_length=50)
    directions = models.TextField()
    tools = models.CharField(max_length=100)

def __str__(self):
    return self.title