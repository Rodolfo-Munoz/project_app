from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Recipe, TempRecords, Product, Supplier, Order, OrderDetail
from .forms import RecipeForm, TempForm, ProductForm, SupplierForm, OrderForm, OrderDetailForm

# Pagination imports
from django.core.paginator import Paginator


def home(request):
    return render(request, 'roseleaf_app/home.html', {})


def login(request):
    if request.method == 'GET':
        return render(request, 'roseleaf_app/login.html',
                      {'form': AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          'roseleaf_app/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            return redirect('home')


def logout(request):
    logout(request)
    return redirect('login')


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
    product_list = Product.objects.all()

    # Set up pagination
    p = Paginator(Product.objects.all().order_by('name'), 8)
    page = request.GET.get('page')
    product_page = p.get_page(page)
    nums = 'a' * product_page.paginator.num_pages

    return render(request, 'roseleaf_app/products.html',
                  {'product_list': product_list,
                   'product_page': product_page,
                   'nums': nums})


def new_product(request):
    submitted = False
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_product?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True

    form = ProductForm
    return render(request, 'roseleaf_app/new_product.html', {'form': form, 'submitted': submitted})


def show_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'roseleaf_app/show_product.html', {'product': product})


def search_product(request):
    searched = request.POST.get('searched')
    product_searched = Product.objects.filter(supplier__name__contains=searched) | Product.objects.filter(
        name__contains=searched) | Product.objects.filter(area__name__contains=searched) | Product.objects.filter(
        product_type__product_type__contains=searched)

    return render(request, 'roseleaf_app/search_product.html',
                  {'searched': searched, 'product_searched': product_searched})


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'roseleaf_app/update_product.html',
                  {'product': product, 'form': form})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products')


def list_recipes(request):
    recipe_list = Recipe.objects.all()

    # Set up pagination
    p = Paginator(Recipe.objects.all().order_by('name'), 8)
    page = request.GET.get('page')
    recipe_page = p.get_page(page)
    nums = 'a' * recipe_page.paginator.num_pages

    return render(request, 'roseleaf_app/list_recipes.html',
                  {'recipe_list': recipe_list,
                   'recipe_page': recipe_page,
                   'nums': nums})


def show_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'roseleaf_app/show_recipe.html', {'recipe': recipe})


def search_recipes(request):
    searched = request.POST.get('searched')
    recipe_searched = Recipe.objects.filter(name__contains=searched)
    return render(request, 'roseleaf_app/search_recipes.html',
                  {'searched': searched, 'recipe_searched': recipe_searched})


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
                      'temp_page': temp_page,
                      'nums': nums,
                      'temp_list': temp_list})


def show_temp_record(request, temp_record_id):
    temp_record = TempRecords.objects.get(pk=temp_record_id)
    return render(request, 'roseleaf_app/show_temp_record.html', {'temp_record': temp_record})


def delete_temp_record(request, temp_record_id):
    temp_record = TempRecords.objects.get(pk=temp_record_id)
    temp_record.delete()
    return redirect('temp_records')


def new_supplier(request):
    suppliers_list = Supplier.objects.all()
    submitted = False
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_supplier?submitted=True')
    else:
        form = SupplierForm
        if 'submitted' in request.GET:
            submitted = True

    form = SupplierForm
    return render(request, 'roseleaf_app/new_supplier.html', {'form': form,
                                                              'submitted': submitted,
                                                              'suppliers_list': suppliers_list})


def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(pk=supplier_id)
    supplier.delete()
    return redirect('new_supplier')


def orders(request):
    orders_list = Order.objects.all()

    # Set up pagination
    p = Paginator(Order.objects.all().order_by('-date'), 8)
    page = request.GET.get('page')
    orders_page = p.get_page(page)
    nums = 'a' * orders_page.paginator.num_pages

    return render(request, 'roseleaf_app/orders.html',
                  {'orders_list': orders_list,
                   'orders_page': orders_page,
                   'nums': nums})


def show_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'roseleaf_app/show_order.html', {'order': order})


def search_orders(request):
    searched = request.POST.get('searched')
    order_searched = (Order.objects.filter(order_detail__product__name__contains=searched) | Order.objects.filter(
        user__username__icontains=searched)).distinct()

    return render(request, 'roseleaf_app/search_orders.html', {'searched': searched, 'order_searched': order_searched})


def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect('orders')


def new_order(request):
    submitted = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_order?submitted=True')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True

    form = OrderForm
    return render(request, 'roseleaf_app/new_order.html', {'form': form, 'submitted': submitted})


def new_order_detail(request):
    submitted = False
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/new_order_detail?submitted=True')
    else:
        form = OrderDetailForm
        if 'submitted' in request.GET:
            submitted = True

    form = OrderDetailForm
    return render(request, 'roseleaf_app/new_order_detail.html', {'form': form, 'submitted': submitted})
