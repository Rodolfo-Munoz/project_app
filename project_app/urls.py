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
]
