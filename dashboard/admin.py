from django.contrib import admin
from .models import Recipes, userRecipes, Utensils,Ingredients,keywords,process_steps
from django.contrib.auth.models import Group

admin.site.site_header = 'Recipe Management System'

class Recipeadmin(admin.ModelAdmin):
    list_display = ('recipe_id','recipe_name', 'cooking_time')
    list_filter = ('category','recipe_name','cooking_time')

class keywords_admin(admin.ModelAdmin):
    list_display = ('recipe_id','keyword')


class user_recipe_admin(admin.ModelAdmin):
    list_display = ('recipe_id','recipe_name', 'cooking_time')
    list_filter = ('category','recipe_name','cooking_time')


class Utensilsadmin(admin.ModelAdmin):

    list_display = ('utensil_name', 'utensil_id')

class Ingredientsadmin(admin.ModelAdmin):

    list_display = ('ingredient_name', 'ingredient_id')

class process_steps_admin(admin.ModelAdmin):
    list_display = ('recipe_id','ingredient_id', 'step_no','utensil_id','process')


# Register your models here.
admin.site.register(Recipes, Recipeadmin)
admin.site.register(Utensils, Utensilsadmin)
admin.site.register(Ingredients, Ingredientsadmin)
admin.site.register(userRecipes, Recipeadmin)
admin.site.register(keywords, keywords_admin)
admin.site.register(process_steps, process_steps_admin)
#admin.site.unregister(Group)
