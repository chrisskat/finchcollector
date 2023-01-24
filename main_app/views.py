from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch


# from django.http import HttpResponse
# Create your views here.

# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, color, age):
#     self.name = name
#     self.breed = breed
#     self.color = color
#     self.age = age

# finches = [
#   Finch('Pierre', 'Eurasian Bullfinch', 'Orange, Black, Grey', 4),
#   Finch('Dionysios', 'American Goldfinch', 'Black, Yellow', 7),
#   Finch('Bob', 'European Greenfinch', 'Green, Yellow', 5)
# ]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  # success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'color', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'