from django.conf.urls import url
from django.urls import path

from account import urls
from component import views

urlpatterns = [
    path('', views.home, name='home'),
    path('components/<str:name>/', views.components, name='component_tech'),
    path('search/', views.search, name='searching'),
    url('components/', views.component_list, name='component_list'),
    path('component/detail/<int:component_id>/', views.detail_by_id, name='comp_detail_by_id'),
    url('details', views.detail, name='component_detail'),

]
urlpatterns = urlpatterns + urls.urlpatterns
