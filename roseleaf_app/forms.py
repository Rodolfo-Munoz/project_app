from django import forms
from django.forms import ModelForm
from .models import Recipe, TempRecords



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
            'user' : forms.Select(attrs={'class':'form-select'}),
            'season' : forms.Select(attrs={'class':'form-select'}),
            'Ingredients' : forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'placeholder' : 'Add ingredients'}),
            'method' : forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'placeholder' : 'Method'}),
            'allergens' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class TempForm(ModelForm):
    class Meta:
        model = TempRecords
        fields = ('temp_date', 'temperature', 'fridge', 'user')
        labels = {
            'temp_date' : '',
            'temperature' : '',

        }
        widgets = {
            'temp_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'temperature': forms.NumberInput(attrs={'class':'form-control', 'placeholder' : 'Temperature'}),
            'user' : forms.Select(attrs={'class':'form-select'}),
            'fridge' : forms.Select(attrs={'class':'form-select'}),
        }


