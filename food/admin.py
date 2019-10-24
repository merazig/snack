from django.contrib import admin

# Register your models here.
from .models import Pizza, Burger

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prixm', 'prixl')

admin.site.register(Pizza, PizzaAdmin)

class BurgerAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prixm', 'prixl')

admin.site.register(Burger, BurgerAdmin)