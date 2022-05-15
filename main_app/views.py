from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import uuid
import boto3
from .models import Shoe, Occasion, Photo
from .forms import WoreForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def shoes_index(request):
  shoes = Shoe.objects.filter(user=request.user)
  return render(request, 'shoes/index.html', {'shoes': shoes})

@login_required
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
  
class ShoeCreate(LoginRequiredMixin, CreateView):
  model = Shoe
  fields = ['name', 'brand', 'description', 'gender', 'size', 'color', 'price']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ShoeUpdate(LoginRequiredMixin, UpdateView):
  model = Shoe
  # Let's disallow the renaming of a Shoe by excluding the name field!
  fields = ['brand', 'description', 'gender', 'size', 'color', 'price']

class ShoeDelete(LoginRequiredMixin, DeleteView):
  model = Shoe
  success_url = '/shoes/'

@login_required
def add_wore(request, shoe_id):
  form = WoreForm(request.POST)
  if form.is_valid():
    new_wore = form.save(commit=False)
    new_wore.shoe_id = shoe_id
    new_wore.save()
  return redirect('detail', shoe_id=shoe_id)

@login_required
def assoc_occasion(request, shoe_id, occasion_id):
  Shoe.objects.get(id=shoe_id).occasions.add(occasion_id)
  return redirect('detail', shoe_id=shoe_id)

@login_required
def unassoc_occasion(request, shoe_id, occasion_id):
  Shoe.objects.get(id=shoe_id).occasions.remove(occasion_id)
  return redirect('detail', shoe_id=shoe_id)

class OccasionList(LoginRequiredMixin, ListView):
  model = Occasion

class OccasionDetail(LoginRequiredMixin, DetailView):
  model = Occasion

class OccasionCreate(LoginRequiredMixin, CreateView):
  model = Occasion
  fields = '__all__'

class OccasionUpdate(LoginRequiredMixin, UpdateView):
  model = Occasion
  fields = ['name', 'color']

class OccasionDelete(LoginRequiredMixin, DeleteView):
  model = Occasion
  success_url = '/occasions/'

@login_required
def add_photo(request, shoe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, shoe_id=shoe_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', shoe_id=shoe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Programmatically login
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)