from django.contrib import admin
from .models import Bestsellers
from .models import Bestsellers_combos
from .models import New_Launches
from .models import Moisturize
from .models import AllProducts

# Register your models here.

@admin.register(Bestsellers)
class BestsellersAdmin(admin.ModelAdmin):
    list_display =['id', 'name','description','price']

@admin.register(Bestsellers_combos)
class Bestsellers_combosAdmin(admin.ModelAdmin):
    list_display =['id', 'name','description','price']

@admin.register(New_Launches)
class New_LaunchesAdmin(admin.ModelAdmin):
    list_display =['id', 'name','description','price']

@admin.register(Moisturize)
class MoisturizeAdmin(admin.ModelAdmin):
    list_display =['id', 'name','description','price']

@admin.register(AllProducts)
class AllProductsAdmin(admin.ModelAdmin):
    list_display =['id', 'name','description','price']