from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, exceptions, permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import User
from account.serializers import UserSerializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}


class UserAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JWTAuthentication]  # JWT OAuth
    def post(self, request):
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
            raise exceptions.AuthenticationFailed("Invalid Email/Password.")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is not active or deleted.")
        token_data = get_tokens_for_user(user)
        print(token_data)
        return Response({"success": True,
                         "data": token_data
                         }, status=status.HTTP_200_OK)


class Profile(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # JWT OAuth

    # def get(self, request):
    #     user = User.objects.all()
    #     user_serializers = UserSerializers(user)
    #     return Response(data=user_serializers.data, status=status.HTTP_200_OK)
