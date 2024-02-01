
from django.db import models

    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Название категории')
    slug = models.SlugField(verbose_name = 'Это поле автоматически заполняется')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
class Dish(models.Model):
    category = models.ForeignKey(Category, related_name='dishes', on_delete=models.CASCADE, verbose_name = 'Категория')
    name = models.CharField(max_length=255, verbose_name = 'Название')
    description = models.TextField(max_length=255, verbose_name = 'Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Цена')
    image = models.ImageField(upload_to='dish_images/', blank=True, null=True, verbose_name = 'Изображение')
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
