from django.urls import path
from website.views import home, add, add_detail

urlpatterns = [
    path('', home, name='home'),
    path('add', add, name='add'),
    path('addDetail', add_detail, name='add_detail')
]
