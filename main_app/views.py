from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toys
from .forms import FeedingForm



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feedings_form = FeedingForm()
  return render(request, 'finches/detail.html', { 
    'finch': finch,
    'feedings_form': feedings_form, 
    })

def add_feedings(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feedings = form.save(commit=False)
        new_feedings.finch_id= finch_id
        new_feedings.save()
    return redirect('detail', finch_id=finch_id)  

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