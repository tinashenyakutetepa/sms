from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from stock.models import Stock
from .serializers import StockSerializer

@api_view(['GET'])
def stockList_api(request):
	stockList = Stock.objects.all().order_by('-id')
	serializer = StockSerializer(stockList, many=True)
	return Response(serializer.data)