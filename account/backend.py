from django.contrib.auth import get_user_model, authenticate
from rest_framework import authentication, exceptions, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.settings import api_settings


class CustomAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        message=""
        success = True
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                success = False
                message = e.args[0]

        raise InvalidToken({
            'success': success,
            'message': message
        })

    def authenticate(self, request):
        if self.get_header(request) is None:
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
            return user, None
        else:
            header = self.get_header(request)
            if header is None:
                return None
            raw_token = self.get_raw_token(header)
            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), None


class InvalidToken(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Invalid Token')
    default_code = 'token_not_valid'
