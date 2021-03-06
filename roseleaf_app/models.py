from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Season(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Fridge(models.Model):
    fridge_name = models.CharField(max_length=50)

    def __str__(self):
        return self.fridge_name


class TempRecords(models.Model):
    temp_date = models.DateField()
    temperature = models.IntegerField()
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.temp_date)


class Allergen(models.Model):
    allergen_name = models.CharField(max_length=20)

    def __str__(self):
        return self.allergen_name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True, blank=True)
    Ingredients = models.CharField(max_length=300)
    method = models.CharField(max_length=300)
    allergens = models.ManyToManyField('Allergen')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    product_type = models.CharField(max_length=20)

    def __str__(self):
        return self.product_type


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product.name) + ' - ' + str(self.quantity) + ' units'


class Order(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    order_detail = models.ManyToManyField('OrderDetail', default=None,)

    def __str__(self):
        return str(self.date)








