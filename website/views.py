from django.shortcuts import render, redirect
from component.models import Detail

from django.forms import modelform_factory

DetailForm = modelform_factory(Detail, exclude=[])

# Create your views here.

def home(request):
    return render(request, 'website/home.html')

def add(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DetailForm()

    return render(request,
                  'website/add.html',
                  context={'form': form})
