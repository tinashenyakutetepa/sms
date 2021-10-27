from django.urls import path
from .import views

urlpatterns = [
    path('',views.stockList_api, name="stocklist-api"),    
]
