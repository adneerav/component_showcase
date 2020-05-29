from django.urls import path

from account import api, views

urlpatterns = [
    # path('account/', api.UserAPI.as_view(), name='account_api'),
    path('login/', views.login, name='login'),
    path('singup/', views.signup, name='signup'),
    path('createaccount/', views.create_account, name='create_account'),
    path('api/login/', api.UserAPI.as_view(), name='loginapi'),
    path('profile/', api.Profile.as_view(), name='profile'),
    path('welcome/', views.welcome, name='welcome')
]
