from django.urls import path
from .views import menu_list, category_detail

app_name = 'menu'

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('category/<slug:category_slug>/', category_detail, name='category_detail'),
]

