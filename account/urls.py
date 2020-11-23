from django.conf.urls import url
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from account import api, views

schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    # path('account/', api.UserAPI.as_view(), name='account_api'),
    url(r'^docs/', schema_view),
    path('login/', views.login, name='login'),
    path('singup/', views.signup, name='signup'),
    path('createaccount/', views.create_account, name='create_account'),
    path('api/login/', api.UserAPI.as_view(), name='loginapi'),
    path('api/createaccount/', api.Registration.as_view(), name='createaccount'),
    path('api/profile/', api.Profile.as_view(), name='profile'),
    path('welcome/', views.welcome, name='welcome')
]
