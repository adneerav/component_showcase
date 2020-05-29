import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from account.models import User
from account.serializers import UserSerializers


def login(request):
    return render(request, 'account/login.html', {})


def signup(request):
    return render(request, 'account/signup.html', {})


def create_account(request):
    if request.method == 'POST' and request.is_ajax():
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        password = request.POST["password"]
        print("{} {} {}".format(fullname, email, password))
        user = User.objects.filter(email=email).exists()
        if user:
            return JsonResponse(
                {
                    "success": False,
                    "message": "User already exist with this email."
                }, status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.create_user(
            username=email.split("@")[0],
            full_name=fullname,
            email=email,
            password=password,
            active=True,
        )
        serializer = UserSerializers(user)
        return JsonResponse(
            {
                "success": True,
                "data": serializer.data
            }, status=status.HTTP_200_OK
        )
    else:
        return JsonResponse(
            {"success": False}, status=status.HTTP_400_BAD_REQUEST
        )


def welcome(request):
    return render(request, "account/welcome.html", {})
