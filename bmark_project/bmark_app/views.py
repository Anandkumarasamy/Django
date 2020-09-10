from django.shortcuts import render
from bmark_app.models import Customer,Bookmark,CustomerBookmark
from bmark_app.serializers import Customer_serializer,Bookmark_serializer,CustomerBookmark_serializer

from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.
class Customerlist(APIView):

    def get(self, request, format=None):
        #--------gettin fields from table
        customer=Customer.objects.all()
        #bookmark=Bookmark.objects.only('title','source_name')
        #customerbookmark=CustomerBookmark.only('BookMark_date')
        #--------serialization
        serializer_get=Customer_serializer(customer,many=True)
        #book_serializer=Bookmark_serializer(bookmark,many=True)
        #custo_book_serializer=CustomerBookmark_serializer(customerbookmark)
        #--------append json
        #serializer=json.loads(custo_serializer)
        #serializer.update(book_serializer)
        #--------return json
        return Response(serializer_get.data)
    def post(self, request, format=None):
        data = Customer.objects.create(
            cus_name=request.POST.get('cus_name'),
            geo_lat=request.POST.get('geo_lat'),
            geo_long=request.POST.get('geo_long')
        )
        serializer_post = Customer_serializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data, status=status.HTTP_201_CREATED)
        return Response(serializer_post.errors, status=status.HTTP_400_BAD_REQUEST)
