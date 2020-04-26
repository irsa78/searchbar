# from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

admin.site.register(City, CityAdmin)
# youtube
from .models import Author, Category, Journal

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Journal)

from .models import Scholarship,Country,Citty
admin.site.register(Scholarship)
admin.site.register(Country)
admin.site.register(Citty)