from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from stock.models import Stock
from .serializers import StockSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/api/stock-list/',
		'Detail View':'/api/stock-detail/id/',
		'Create':'/api/create-stock/',
		'Update':'/api/update-stock/id/',
		'Delete':'/api/delete-stock/id/',
		}

	return Response(api_urls)

@api_view(['GET'])
def stockList_api(request):
	stockList = Stock.objects.all().order_by('-id')
	serializer = StockSerializer(stockList, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def stockDetail(request, pk):
	stock = Stock.objects.get(id=pk)
	serializer = StockSerializer(stock, many=False)
	return Response(serializer.data)

@api_view(['DELETE'])
def deleteStock(request, pk):
	stock = Stock.objects.get(id=pk)
	stock.delete()

	return Response('Item succsesfully delete!')


@api_view(['POST'])
def createStock(request):
	serializer = StockSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
	

@api_view(['POST'])
def updateStock(request, pk):
	stock = Stock.objects.get(id=pk)
	serializer = StockSerializer(instance=stock, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)