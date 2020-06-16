from django.shortcuts import render, HttpResponse
from details.models import ApiView
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ApiViewSerializer
from .filters import ApiViewFilters
from rest_framework import filters, status
from rest_framework import generics
import csv

@api_view(['GET'])
def index(request):
    context = {
        "first_name": "raj",
        "last_name": "kumar",
        "address": "Tamilnadu, India",
    }
    return render(request, 'index.html', context)

@api_view(['GET', 'POST'])
def student_list(request):
    with open('students.txt') as csvfile:
        data = csv.DictReader(csvfile)
        objs = [
            ApiView(
                stu_name=row['stu_name'],
                stu_age=row['stu_age'],
                stu_class=row['stu_class'],
                stu_location=row['stu_location'],
                stu_gender = row['stu_gender']
            )
            for row in data
        ]

        datas = ApiView.objects.bulk_create(objs=objs)
        db = requests.post('http://127.0.0.1:8000/students/', data=datas)
        return HttpResponse("created")


@api_view(['GET'])
def search_api(request):
    data = ApiViewFilters(request.GET)
    return render(request, 'templates.html', {'filter': data})


class UserListView(generics.ListAPIView):
    queryset = ApiView.objects.all()
    serializer_class = ApiViewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['stu_location', 'stu_gender']


@api_view(['GET', 'PUT', 'DELETE'])
def newone(request, pk):
    try:
        api = ApiView.objects.get(id=pk)
    except:
        return Response(status=status.Http_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiViewSerializer(api)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiViewSerializer(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        api.delete()
        return Response(status=status.Http_404_NOT_FOUND)
