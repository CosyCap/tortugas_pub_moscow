from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно завершено!")
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
            messages.success(request, "Бронирование успешно завершено!")
            print("Data saved successfully")
            return redirect('main:reservation')  # Перенаправление на другую страницу после успешного сохранения
        else:
            print("Form errors:", form.errors.as_text())
    else:
        form = ReservationForm()
    
    return render(request, 'main/reservation.html', {'form': form})
