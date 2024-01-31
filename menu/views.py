from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

def menu_list(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    category_filter = request.GET.get('category', None)

    if category_filter:
        dishes = dishes.filter(category__slug=category_filter)

    context = {'dishes': dishes, 'categories': categories, 'category_filter': category_filter}
    return render(request, 'menu/menu.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    dishes = Dish.objects.filter(category=category)

    context = {'category': category, 'dishes': dishes}
    return render(request, 'menu/category_detail.html', context)
