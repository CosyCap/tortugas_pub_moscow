from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255, verbose_name = 'Имя')
    phone = models.CharField(max_length=15, default='0', verbose_name = 'Номер телефона')
    num_persons = models.PositiveIntegerField(verbose_name = 'Количество человек')
    date = models.DateField(verbose_name = 'Дата посещения')
    time = models.TimeField(null=True, verbose_name = 'Время посещения')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
    
