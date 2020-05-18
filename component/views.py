from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_list_or_404

# Create your views here.
from component.models import Component, Detail
from technology.models import Technology
