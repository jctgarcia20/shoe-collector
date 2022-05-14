from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shoe
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
  wore_form = WoreForm()
  return render(request, 'shoes/detail.html', {
    'shoe': shoe,'wore_form': wore_form
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