from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Recipe, TempRecords
from .forms import RecipeForm, TempForm

# Pagination imports
from django.core.paginator import Paginator

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
    submitted = False
    if request.method == 'POST':
        form = TempForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/temperatures?submitted=True')
    else:
        form = RecipeForm
        if 'submitted' in request.GET:
            submitted = True

    form = TempForm
    return render(request, 'roseleaf_app/temperatures.html', {'form': form, 'submitted': submitted})





def products(request):
    return render(request, 'roseleaf_app/products.html', {})


def orders(request):
    return render(request, 'roseleaf_app/orders.html', {})


def list_recipes(request):
    recipe_list = Recipe.objects.all()

    # Set up pagination
    p = Paginator(Recipe.objects.all().order_by('name'), 5)
    page = request.GET.get('page')
    recipe_page = p.get_page(page)
    nums = 'a' * recipe_page.paginator.num_pages

    return render(request, 'roseleaf_app/list_recipes.html',
                  {'recipe_list' : recipe_list,
                   'recipe_page' : recipe_page,
                   'nums': nums})


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


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    return redirect('list_recipes')


def temp_records(request):
    temp_list = TempRecords.objects.all()

    # Set up pagination
    p = Paginator(TempRecords.objects.all().order_by('-temp_date'), 10)
    page = request.GET.get('page')
    temp_page = p.get_page(page)
    nums = 'a' * temp_page.paginator.num_pages

    return render(request, 'roseleaf_app/temp_records.html',
                  {
                   'temp_page' : temp_page,
                   'nums': nums,
                   'temp_list' : temp_list})


def show_temp_record(request, temp_record_id):
    temp_record = TempRecords.objects.get(pk=temp_record_id)
    return render(request, 'roseleaf_app/show_temp_record.html', {'temp_record' : temp_record})


def delete_temp_record(request, temp_record_id):
    temp_record = TempRecords.objects.get(pk=temp_record_id)
    temp_record.delete()
    return redirect('temp_records')




