from django import forms
from django.forms import ModelForm
from .models import Recipe
from .models import Ingredient


# create a recipe form
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        labels = {
            'name' : '',
            'description' : '',
            'method' : '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Recipe name'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Description'}),
            'user' : forms.Select(attrs={'class':'form-control'}),
            'season' : forms.Select(attrs={'class':'form-control'}),
            'Ingredients' : forms.SelectMultiple(attrs={'class':'form-control'}),
            'method' : forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'placeholder' : 'Method'}),
            'allergens' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)
        labels = {'name' : ''}
        widgets = {'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Add an ingredient'}),}