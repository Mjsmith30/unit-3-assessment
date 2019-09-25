from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView 
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

# Create your views here.

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'add.html'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    fields = '__all__'
    template_name = 'item_confirm_delete.html'
    success_url = '/'

       

      
def ItemList(request):
    items = Item.objects.all()
    return render(request, '/home.html', {'items': items})    

