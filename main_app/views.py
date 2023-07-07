from django.shortcuts import render, get_object_or_404
from .models import Finch
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
    finches = [
        {"name": "Finch 1", "color": "Red", "size": "Small"},
        {"name": "Finch 2", "color": "Yellow", "size": "Medium"},
        {"name": "Finch 3", "color": "Blue", "size": "Large"},
    ]
    return render(request, "main_app/index.html", {"finches": finches})

def index(request):
    finches = Finch.objects.all()
    return render(request, "main_app/index.html", {"finches": finches})

def details(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, "main_app/details.html", {"finch": finch})




class FinchCreateView(CreateView):
    model = Finch
    fields = ['name', 'color', 'size']
    success_url = reverse_lazy('index')

class FinchUpdateView(UpdateView):
    model = Finch
    fields = ['name', 'color', 'size']
    success_url = reverse_lazy('index')

class FinchDeleteView(DeleteView):
    model = Finch
    success_url = reverse_lazy('index')
