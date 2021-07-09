from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(requset):
    return HttpResponse("Hello, World!")


@api_view(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return Response({"data": "123"})

    elif request.method == "POST":
        if request.data["id"] == "abcd" and request.data["password"] == "1234":
            return Response({"result": True})
        else:
            return Response({"result": False})


# Create your views here.
