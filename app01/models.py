from django.db import models


# Create your models here.


class Admin(models.Model):
    """ 管理员 """
    username = models.CharField(verbose_name="Username", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)

    def __str__(self):
        return self.username


class Menu(models.Model):
    """ all meun """
    name = models.CharField(verbose_name="Name", max_length=32)
    time = models.IntegerField(verbose_name="time need to be done")

    tem = models.IntegerField(verbose_name="temperature")
    inter = models.CharField(verbose_name="materials needed", max_length=256)
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='Menu/')


class meat(models.Model):
    """ The ingredients """
    meat = models.CharField(verbose_name="Meat", max_length=16, default="Beef")
    quantity = models.IntegerField(default=1, verbose_name="Amount")

    def __str__(self):
        return self.meat


class Auxiliary(models.Model):
    """ The ingredients """
    aux = models.CharField(verbose_name="aux", max_length=16, default="Salt")

    quantity = models.IntegerField(default=1, verbose_name="Amount")

    def __str__(self):
        return self.aux


class vegetable(models.Model):
    """ The ingredients """
    veg = models.CharField(verbose_name="vegetable", max_length=16, default="coriander")
    quantity = models.IntegerField(default=1, verbose_name="Amount")

    def __str__(self):
        return self.veg


class home(models.Model):
    """ The data in home page"""

    name = models.CharField(verbose_name="Name", max_length=64)
    temperature = models.IntegerField(verbose_name="Temperature", default=0)
    time = models.IntegerField(verbose_name="Time")
    utensils = models.CharField(verbose_name="Utensils", max_length=128)
    cate_food = (
        (1, "Most popular"),
        (2, "Best taste"),
        (3, "Vegetarianism"),
        (4, "Gorgeous"),
        (5, "Fast speed"),
        (6, "Breakfast"),
        (7, "Homely recipes"),
        (8, "Baking"),
        (9, "Children's food"),
        (10, "Baking"),
        (11, "Stape Food"),
        (12, "Dessert"),
        (13, "Snack"),
        (14, "Western Food"),
    )
    cate = models.SmallIntegerField(verbose_name="Category", choices=cate_food, default=1)
    description = models.TextField(verbose_name="Description", max_length=256, default="Delicious")
    meat = models.ForeignKey('meat', models.CASCADE)
    auxiliary = models.ForeignKey('Auxiliary', models.CASCADE)
    veg = models.ForeignKey('vegetable', models.CASCADE)
    quan = models.IntegerField(verbose_name="Amount", default=1)

    steps = models.TextField(verbose_name="Steps", max_length=500)
    Rate_stars = (
        (1, "One star"),
        (2, "Two stars"),
        (3, "Three stars"),
        (4, "Four stars"),
        (5, "Five stars"),
    )
    rate = models.IntegerField(verbose_name="Rate", choices=Rate_stars, default=3)
    calories = models.DecimalField(verbose_name="Calories", max_digits=6, decimal_places=2, default=300)
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='Menu/', default='Menu/10.jpeg')


class favorite(models.Model):
    """ The data in home page"""
    name = models.CharField(verbose_name="Name", max_length=64)
    temperature = models.IntegerField(verbose_name="Temperature", default=0)
    time = models.IntegerField(verbose_name="Time")
    utensils = models.CharField(verbose_name="Utensils", max_length=128)
    cate_food = (
        (1, "Most popular"),
        (2, "Best taste"),
        (3, "Vegetarianism"),
        (4, "Gorgeous"),
        (5, "Fast speed"),
        (6, "Breakfast"),
        (7, "Homely recipes"),
        (8, "Baking"),
        (9, "Children's food"),
        (10, "Baking"),
        (11, "Stape Food"),
        (12, "Dessert"),
        (13, "Snack"),
        (14, "Western Food"),
    )
    cate = models.SmallIntegerField(verbose_name="Category", choices=cate_food, default=1)
    description = models.TextField(verbose_name="Description", max_length=256, default="Delicious")
    meat = models.ForeignKey('meat', models.CASCADE)
    auxiliary = models.ForeignKey('Auxiliary', models.CASCADE)
    veg = models.ForeignKey('vegetable', models.CASCADE)
    quan = models.IntegerField(verbose_name="Amount", default=1)

    steps = models.TextField(verbose_name="Steps", max_length=500)
    Rate_stars = (
        (1, "One star"),
        (2, "Two stars"),
        (3, "Three stars"),
        (4, "Four stars"),
        (5, "Five stars"),
    )
    rate = models.IntegerField(verbose_name="Rate", choices=Rate_stars, default=3)
    calories = models.DecimalField(verbose_name="Calories", max_digits=6, decimal_places=2, default=300)
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='Menu/', default='Menu/10.jpeg')

