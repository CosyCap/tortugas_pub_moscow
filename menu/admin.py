from django.contrib import admin
from .models import Dish, Category

def delete_all_categories(modeladmin, request, queryset):
    queryset.delete()

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    actions = [delete_all_categories]
