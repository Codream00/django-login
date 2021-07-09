import re
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Addresses
from .serializers import AddressesSerializer


@api_view(["GET", "POST"])
def address_list(request):
    if (request.method) == "GET":
        query_set = Addresses.objects.all()
        serializer = AddressesSerializer(query_set, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)

    if request.method == "GET":
        serializer = AddressesSerializer(obj)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = request.data
        serializer = AddressesSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        obj.delete()
        return Response(status=204)


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = request.data
        search_id = data["userId"]
        obj = Addresses.objects.get(userId=search_id)

        if data["password"] == obj.password:
            return Response(status=200)
        else:
            return Response(status=400)


# Create your views here.
