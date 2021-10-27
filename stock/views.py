from typing import ContextManager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StockForm
from .models import Stock
# Stock views here.


def stock(request):
    db_objects = Stock.objects.all()
    total_Number_of_Iterms = Stock.objects.all().count()
    
    form = StockForm()

    if request.method == 'POST':
        form = StockForm(request.POST or None,request.FILES or None)
        if form.is_valid:
            form.save()
    else:
        form = StockForm()

    context = {
        'title':'Stock Page',
        'db_objects': db_objects,
        'total_Number_of_Iterms' : total_Number_of_Iterms,
        'form': form,
        
        }
    return render(request,'stock/index.html', context)


# === Delete Stock ====
def delete_stock_item_view(request, pk):
    item = Stock.objects.get(id=pk)
    item.delete()    

    return redirect('stock')
# === Delete Stock ====


 # === Update Stock ====
def update_stock_item_view(request, pk):
    item = Stock.objects.get(id=pk)
    form = StockForm(instance=item)

    if request.method == 'POST':
        form = StockForm(request.POST or None, request.FILES or None, instance=item)

        if form.is_valid():
            form.save()            
            return redirect('stock')

    context = {
        'form': form,
    }
    return render(request, 'stock/index.html', context)
# === Update Stock ====



























#Pages
def home(request):
    context = {
        'title':'Home Page'
    }
    return render(request,'stock/index.html', context)

def contact(request):
    context = {
        'title':'Contact Us'
    }
    return render(request,'stock/index.html', context)
