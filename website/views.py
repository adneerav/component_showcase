from django.shortcuts import render, redirect
from component.models import Detail, Component

from django.forms import modelform_factory

ComponentInstance = modelform_factory(Component, exclude=[])
DetailInstance = modelform_factory(Detail, exclude=[])


# Create your views here.

def home(request):
    components = Detail.objects.all()
    components_count = Detail.objects.count()
    return render(request, 'website/home.html', {
        'components_count': components_count,
        'components': components
    })


def add(request):
    if request.method == 'POST':
        form = ComponentInstance(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_detail')
    else:
        form = ComponentInstance()

    return render(request,
                  'website/add.html',
                  context={'form': form})


def add_detail(request):
    if request.method == 'POST':
        form = DetailInstance(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DetailInstance()

    return render(request,
                  'website/add_detail.html',
                  context={'form': form})
