from django.db import models


class Member(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Fridge(models.Model):
    fridge_name = models.CharField(max_length=50)

    def __str__(self):
        return self.fridge_name


class TempRecords(models.Model):
    temp_date = models.DateTimeField()
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
    Ingredients = models.CharField(max_length=200)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    method = models.CharField(max_length=300)

    def __str__(self):
        return self.name
