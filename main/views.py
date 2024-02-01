from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
import locale

def index(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно завершено! Скоро Вам перезвоним чтобы уточнить детали")
            print("Data saved successfully")
            return redirect('main:index')  # Перенаправление на другую страницу после успешного сохранения
        else:
            print("Form errors:", form.errors.as_text())
    else:
        form = ReservationForm()

    return render(request, 'main/index.html', {'form': form})

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно завершено! Скоро Вам перезвоним чтобы уточнить детали")
            print("Data saved successfully")
            return redirect('main:reservation')  # Перенаправление на другую страницу после успешного сохранения
        else:
            print("Form errors:", form.errors.as_text())
    else:
        form = ReservationForm()
    
    return render(request, 'main/reservation.html', {'form': form})

from django.shortcuts import render
from datetime import datetime, time
import locale

def working_hours_data(request):
    opening_hours = {
        "пн": "с 8:00 до 23:00",
        "вт": "с 8:00 до 23:00",
        "ср": "с 8:00 до 23:00",
        "чт": "с 8:00 до 23:00",
        "пт": "с 8:00 до 01:00",
        "сб": "с 13:00 до 01:00",
        "вс": "с 13:00 до 01:00",
    }
    week_days = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    working_hours = [15, 15, 15, 15, 17, 12, 12]
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    today = datetime.now().strftime("%a").lower()[:2]  # Convert to lowercase

    current_day_index = week_days.index(today)
    current_working_hours = working_hours[current_day_index]
    current_opening_hours = opening_hours[today]

    # Преобразуйте текущее время из строки в объект datetime.time
    current_opening_hours_start, current_opening_hours_end = map(
        lambda x: time(*map(int, x.split(':'))),
        current_opening_hours.replace('с ', '').replace(' до ', '').split()
    )

    context = {
        "opening_hours": opening_hours,
        "chart_data": {
            "days_of_week": week_days,
            "working_hours": working_hours,
            "current_day": today,
            "current_opening_hours_start": current_opening_hours_start,
            "current_opening_hours_end": current_opening_hours_end,
            "current_working_hours": current_working_hours,
        }
    }

    return render(request, 'base.html', context)