from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, default='0')
    email = models.EmailField(default='', blank=True, unique=False)
    num_persons = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
