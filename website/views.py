from django.shortcuts import render, redirect
from django.template.defaulttags import register

from component.models import Detail, Component
from technology.models import Technology

from django.forms import modelform_factory

ComponentInstance = modelform_factory(Component, exclude=[])
DetailInstance = modelform_factory(Detail, exclude=[])


# Create your views here.

# @register.simple_tag
# def related_deltas():
#     return "Hiii"

def home(request):
    components = Detail.objects.all()
    components_count = Detail.objects.count()
    technologies = Technology.objects.all()

    if (request.method == 'GET'):
        print(request.GET)

    return render(request, 'website/index.html', {
        'components_count': components_count,
        'components': components,
        'technologies': technologies
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
