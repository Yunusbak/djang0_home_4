from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm

def cars_page(request):
    car = Car.objects.all()
    return render(request, 'cars_page.html', {'car': car})

def car_detail(request, pk):
    car = get_object_or_404(car, pk=pk)
    return render(request, 'car_title.html', {"car": car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cars_page")
    else:
        form = CarForm()
    return render(request, 'car_edit.html', {'form': form})

def car_update(request, pk):
    book = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = CarForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def car_delete(request, pk):
    book = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


