"""project_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from roseleaf_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('temperatures/', views.temperatures, name='temperatures'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('list_recipes/', views.list_recipes, name='list_recipes'),
    path('show_recipe/<recipe_id>', views.show_recipe, name='show_recipe'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('update_recipe/<recipe_id>', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('temp_records/', views.temp_records, name='temp_records'),
    path('show_temp_record/<temp_record_id>', views.show_temp_record, name='show_temp_record'),
    path('delete_temp_record/<temp_record_id>', views.delete_temp_record, name='delete_temp_record'),
    path('show_product/<product_id>', views.show_product, name='show_product'),
    path('search_product/', views.search_product, name='search_product'),
    path('new_product/', views.new_product, name='new_product'),
    path('new_supplier/', views.new_supplier, name='new_supplier'),
    path('update_product/<product_id>', views.update_product, name='update_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
    path('delete_supplier/<supplier_id>', views.delete_supplier, name='delete_supplier'),
    path('show_order/<order_id>', views.show_order, name='show_order'),
    path('search_orders/', views.search_orders, name='search_orders'),
    path('delete_order/<order_id>', views.delete_order, name='delete_order'),
    path('new_order/', views.new_order, name='new_order'),
    path('new_order_detail/', views.new_order_detail, name='new_order_detail'),


]
