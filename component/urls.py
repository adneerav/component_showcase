from django.conf.urls import url
from django.urls import path
from component import views

# app_name = "component"
urlpatterns = [
    path('', views.home, name='home'),
    path('components/<str:name>/', views.components, name='component_tech'),
    url('components/', views.component_list, name='component_list'),
    path('component/detail/<int:component_id>/', views.detail_by_id, name='comp_detail_by_id'),
    url('details', views.detail, name='component_detail'),

]
