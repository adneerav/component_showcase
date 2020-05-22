from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from account.models import User

from account.serializers import UserSerializers


class UserAPI(generics.CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
