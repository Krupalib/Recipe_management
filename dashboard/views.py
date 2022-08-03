from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Recipes, userRecipes, Utensils,Ingredients,keywords,process_steps

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def recipe(request):
    recipe_list = Recipes.objects.all()
    recipe_dict = {'recipe' : recipe_list}
    Ingredients_list = Ingredients.objects.all()
    keyword_list = keywords.objects.all()
    result = list()
    name_of_recipe_flag = False
    cooking_time_flag = False
    if "name_of_recipe" in request.GET or "cooking_time" in request.GET:
        if "name_of_recipe" in request.GET:
            name_of_recipe = request.GET["name_of_recipe"]
            name_of_recipe_flag = True

        if  "cooking_time" in request.GET:
            cooking_time = request.GET["cooking_time"]
            cooking_time_flag = True

    if "name_of_recipe" in request.GET and "cooking_time" in request.GET:
            filtered_recipes_for_name_cooking_time = Recipes.objects.filter(recipe_name__icontains = name_of_recipe).filter(cooking_time__icontains = cooking_time)
    elif "name_of_recipe" in request.GET:
             filtered_recipes_for_name_cooking_time = Recipes.objects.filter(recipe_name__icontains = name_of_recipe)
    elif "cooking_time" in request.GET :
            filtered_recipes_for_name_cooking_time = Recipes.objects.filter(cooking_time__icontains = cooking_time)
    else:
            filtered_recipes_for_name_cooking_time = Recipes.objects.all()

###############3############################################################################################33
    name_of_ingredient_flag = False
    keyword_flag = False

    if "name_of_ingredient" in request.GET:
        name_of_ingredient_flag = True
        ingredient = request.GET["name_of_ingredient"]
        filtered_recipes_for_ingredient = list(process_steps.objects.filter(ingredient_id__ingredient_name__icontains = ingredient))
    if "keyword" in request.GET:
        keyword_flag = True
        keyword = request.GET["keyword"]
        filtered_recipes_for_keyword = list(keywords.objects.filter(keyword__icontains = keyword))


    if name_of_ingredient_flag and keyword_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_keyword:
                for y in filtered_recipes_for_ingredient:
                    if (rec.recipe_id == x.recipe_id.recipe_id == y.recipe_id.recipe_id):
                        result.append(rec)

    elif name_of_ingredient_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_ingredient:
                if (rec.recipe_id == x.recipe_id.recipe_id):
                    result.append(rec)

    elif keyword_flag:
        for rec in filtered_recipes_for_name_cooking_time:
            for x in filtered_recipes_for_keyword:
                if (rec.recipe_id == x.recipe_id.recipe_id):
                    result.append(rec)
    elif cooking_time_flag or name_of_recipe_flag:
        result = filtered_recipes_for_name_cooking_time
    else:
        result = recipe_list

    return render(request, 'dashboard/Recipe.html', {'recipe' : result, 'ingredient' : Ingredients_list, 'keyword' : keyword_list})

def process(request):
    webpage_list = process_steps.objects.order_by('step_no')
    date_dict = {'access_records' : webpage_list}

def steps(request,id):
    process = list()
    alldata = process_steps.objects.all()
    process = list(process_steps.objects.filter(recipe_id__recipe_id__icontains = id))
    n = len(process)
    for i in range(1,n):
        already_sorted = True
        for j in range(n - i - 1):
            if process[j].step_no > process[j + 1].step_no:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    process[j], process[j + 1] = process[j + 1], process[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False
            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate



    process = list()
    alldata = process_steps.objects.all()



    process = list(process_steps.objects.filter(recipe_id__recipe_id__icontains = id))
    x = Recipes.objects.filter(recipe_id__icontains = id)
    max_step = None
    for x in process:
        if max_step == None or x.step_no > max_step:
            max_step = x.step_no

        steps_list = list()
        if already_sorted:
            break
    process_dict = {'process' : process}
    return render(request,'dashboard/steps.html', {'process' : process,'recipe' : x})
