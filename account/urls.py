from django.urls import path

from account import api

urlpatterns = [
    path('account/', api.UserAPI.as_view(), name='account_api')
]
