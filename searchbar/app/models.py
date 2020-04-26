from django.db import models

# Create your models here.
# from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name


    # 2nd youtube video
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Journal(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField()
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# mine
class Citty(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    city = models.ManyToManyField(Citty)
    country = models.ManyToManyField(Country)
    research = models.CharField(max_length=255)
    def __str__(self):
        return self.name



