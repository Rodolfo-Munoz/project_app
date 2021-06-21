from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm



def home(request):
    return render(request, 'roseleaf_app/home.html', {})


def login(request):
    if request.method == 'GET':
        return render(request, 'roseleaf_app/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'roseleaf_app/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            return redirect('home')


def recipes(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'roseleaf_app/recipes.html',
                  {'recipe_list': recipe_list})


def new_recipe(request):
    submitted = False
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_recipe?submitted=True')
    else:
        form = RecipeForm
        if 'submitted' in request.GET:
            submitted = True

    form = RecipeForm
    return render(request, 'roseleaf_app/new_recipe.html', {'form': form, 'submitted': submitted})


def temperatures(request):
    return render(request, 'roseleaf_app/temperatures.html', {})


def products(request):
    return render(request, 'roseleaf_app/products.html', {})


def orders(request):
    return render(request, 'roseleaf_app/orders.html', {})


def list_recipes(request):
    recipe_list = Recipe.objects.all()
    return render(request, 'roseleaf_app/list_recipes.html',
                  {'recipe_list' : recipe_list})


def show_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'roseleaf_app/show_recipe.html', {'recipe' : recipe})


def search_recipes(request):
    searched = request.POST.get('searched')
    recipe_searched = Recipe.objects.filter(name__contains=searched)
    return render(request, 'roseleaf_app/search_recipes.html', {'searched' : searched, 'recipe_searched' : recipe_searched})


def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('list_recipes')
    return render(request, 'roseleaf_app/update_recipe.html',
                  {'recipe': recipe, 'form': form})



