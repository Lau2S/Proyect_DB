from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Order_items
from .serializer import Order_itemsSerializer

class ListCreateOrder_items(generics.ListAPIView):
  queryset = Order_items.objects.all()
  serializer_class = Order_itemsSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = Order_itemsSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)