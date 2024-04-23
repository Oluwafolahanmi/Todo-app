from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseBadRequest)
from .models import health
from .forms import HealthForm

# Create your views here.
def home_health(request):
    todo = []
    Health = health.objects.all()
    form = HealthForm()
   
    if request.method =='POST':
        id_name = request.POST.get("name")
        todo = health.objects.get(name =id_name)
    
    context = {'Health': Health, 'form': form, "todo":todo}
    return render(request, 'index_health.html', context)

def add(request):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            health.objects.create(
                name=form.cleaned_data['name'],
                Age=form.cleaned_data['Age'],
                Address=form.cleaned_data['Address'],
            )
            return redirect('healthapp')
        
        else:
            form = HealthForm()

    return render(request, 'index_health.html', {'form': form})


def discharge(request):
    if request.method == 'POST':
        id_name = request.POST.get("name")
        patient_id = health.objects.get(name =id_name)
        patient_id.Discharge_status = True
        patient_id.save()
        return redirect('healthapp')


    


