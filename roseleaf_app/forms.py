from django import forms
from django.forms import ModelForm
from .models import Recipe, TempRecords, Product, Supplier, Order, OrderDetail



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

# Temperature records form
class TempForm(ModelForm):
    class Meta:
        model = TempRecords
        fields = ('temp_date', 'fridge', 'temperature', 'user')
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


# create a new product form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'name' : '',
            'price' : '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Product name'}),
            'supplier': forms.Select(attrs={'class':'form-select'}),
            'product_type' : forms.Select(attrs={'class':'form-select'}),
            'area' : forms.Select(attrs={'class':'form-select'}),
            'price' : forms.NumberInput(attrs={'class':'form-control', 'placeholder' : 'Price'}),

        }


# create a new suppliers form
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        labels = {
            'name' : '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Supplier name'}),

        }


# create a new order form
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        labels = {
            'date' : '',
        }

        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'order_detail': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


# create a new order detail form
class OrderDetailForm(ModelForm):
    class Meta:
        model = OrderDetail
        fields = "__all__"
        labels = {
            'quantity' : '',
        }

        widgets = {
            'product': forms.Select(attrs={'class': 'form-select' }),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        }