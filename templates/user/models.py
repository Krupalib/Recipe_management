from django.db import models

# Create your models here.
CATEGORY = (
      ('Breakfast', 'Breakfast'),
      ('Lunch', 'Lunch'),
      ('Dinner', 'Dinner'),
)
class Recipes(models.Model):
    name = models.CharField(max_length = 100, null=True)
    ingredients = models.CharField(max_length = 100, null=True)
    time = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length = 200, choices = CATEGORY)

    def  __str__(self):
        return f'{self.name}-{self.time}'

class userRecipes(models.Model):
    name = models.CharField(max_length = 100, null=True)
    ingredients = models.CharField(max_length = 100, null=True)
    time = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length = 200, choices = CATEGORY)

    def  __str__(self):
        return f'{self.name}-{self.staff.username}'  
