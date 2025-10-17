from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'founded_year', 'country']
    list_filter = ['country']
    search_fields = ['name']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    list_filter = ['car_make', 'type', 'year']
    search_fields = ['name', 'car_make__name']

# Registering models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)