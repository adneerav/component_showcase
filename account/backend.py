from django.contrib.auth import get_user_model, authenticate
from rest_framework import authentication, exceptions


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request, email=None, password=None):
        email = request.data["email"]
        password = request.data["password"]
        if not email and not password:
            raise exceptions.AuthenticationFailed("Credentials required.")
        credentials = {
            get_user_model().USERNAME_FIELD: email,
            'password': password
        }
        user = authenticate(**credentials)
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Email/Password")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is not active or deleted.")
        return (user, None)
