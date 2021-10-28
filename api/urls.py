from django.urls import path
from .import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('stock-list',views.stockList_api, name="stocklist-api"),  
    path('stock-detail/<int:pk>/', views.stockDetail, name="stockDetail-api"), 
    path('delete-stock/<int:pk>/', views.deleteStock, name="deleteStock-api"),  
    path('create-stock/', views.createStock, name="createStock-api"),
    path('update-stock/<int:pk>/', views.updateStock, name="updateStock-api"),
]
