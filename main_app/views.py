from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Occasion
from .forms import WoreForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
  shoes = Shoe.objects.all()
  #                             data context |
  return render(request, 'shoes/index.html', {
    'shoes': shoes,
  })

def shoes_detail(request, shoe_id):
  shoe = Shoe.objects.get(id=shoe_id)
  id_list = shoe.occasions.all().values_list('id')
  occasions_shoe_doesnt_have = Occasion.objects.exclude(id__in=id_list)
  wore_form = WoreForm()
  return render(request, 'shoes/detail.html', {
    'shoe': shoe,
    'wore_form': wore_form,
    'occasions': occasions_shoe_doesnt_have
  })

def add_wore(request, shoe_id):
  # create a ModelForm instance using the data in request.POST
  form = WoreForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the shoe_id assigned
    new_wore = form.save(commit=False)
    new_wore.shoe_id = shoe_id
    new_wore.save()
  return redirect('detail', shoe_id=shoe_id)

class ShoeCreate(CreateView):
  model = Shoe
  fields = '__all__'

class ShoeUpdate(UpdateView):
  model = Shoe
  # Let's disallow the renaming of a Shoe by excluding the name field!
  fields = ['brand', 'description', 'gender', 'size', 'color', 'price']

class ShoeDelete(DeleteView):
  model = Shoe
  success_url = '/shoes/'

def add_wore(request, shoe_id):
  form = WoreForm(request.POST)
  if form.is_valid():
    new_wore = form.save(commit=False)
    new_wore.shoe_id = shoe_id
    new_wore.save()
  return redirect('detail', shoe_id=shoe_id)

def assoc_occasion(request, shoe_id, occasion_id):
  Shoe.objects.get(id=shoe_id).occasions.add(occasion_id)
  return redirect('detail', shoe_id=shoe_id)

def unassoc_occasion(request, shoe_id, occasion_id):
  Shoe.objects.get(id=shoe_id).occasions.remove(occasion_id)
  return redirect('detail', shoe_id=shoe_id)

class OccasionList(ListView):
  model = Occasion

class OccasionDetail(DetailView):
  model = Occasion

class OccasionCreate(CreateView):
  model = Occasion
  fields = '__all__'

class OccasionUpdate(UpdateView):
  model = Occasion
  fields = ['name', 'color']

class OccasionDelete(DeleteView):
  model = Occasion
  success_url = '/occasions/'