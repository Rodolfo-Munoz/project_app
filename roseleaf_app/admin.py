from django.contrib import admin
from .models import *


admin.site.register(Member)
admin.site.register(Fridge)
admin.site.register(TempRecords)
admin.site.register(Allergen)
#admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(Area)
admin.site.register(ProductType)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(OrderDetail)
admin.site.register(Season)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'season')
    ordering = ('name', )
    list_filter = ('user', 'season', 'Ingredients')
    search_fields = ('name', )