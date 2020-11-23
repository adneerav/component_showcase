from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, exceptions, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from account.backend import CustomAuthentication
from account.models import User
from account.serializers import UserSerializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}


class UserAPI(APIView):
    """
    post: To get AccessToken  & Refresh token by using
    user credentials.
    {
    "email": "citmotog@gmail.com",
        "password": "hbdev"
    }
    """
    permission_classes = [permissions.AllowAny, ]
    authentication_classes = [CustomAuthentication]  # JWT OAuth

    def post(self, request, *args, **kwargs):
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
        return Response({
            "success": True,
            "data": token_data
        }, status=status.HTTP_200_OK)


class Registration(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializers(data=request.data)
        try:
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response({"success": True}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"success": False, "detail": e.get_full_details()}, status=status.HTTP_400_BAD_REQUEST)


class Profile(RetrieveAPIView):
    """
    To get User profile details from the access token received
    from Login Api.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # JWT OAuth

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        user_serializers = UserSerializers(user)
        user_serializers.data.pop("password")
        return Response({
            "success": True,
            "data": user_serializers.data
        }, status=status.HTTP_200_OK)
