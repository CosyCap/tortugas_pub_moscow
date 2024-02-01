from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
import locale

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm

def handle_reservation(request, template_name, redirect_name):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно завершено! Скоро Вам перезвоним чтобы уточнить детали")
            print("Data saved successfully")
            return redirect(redirect_name)
        else:
            print("Form errors:", form.errors.as_text())
    else:
        form = ReservationForm()

    return render(request, template_name, {'form': form})

def index(request):
    return handle_reservation(request, 'main/index.html', 'main:index')

def about(request):
    context = {}
    return render(request, 'main/about.html', context)

def reservation(request):
    return handle_reservation(request, 'main/reservation.html', 'main:reservation')


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
    today = datetime.now().strftime("%a").lower()[:2]  

    current_day_index = week_days.index(today)
    current_working_hours = working_hours[current_day_index]
    current_opening_hours = opening_hours[today]

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