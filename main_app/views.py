from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Add the Cat class & list and view function below the imports
class Shoe:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, description, gender, size, color, price):
    self.name = name
    self.brand = brand
    self.description = description
    self.gender = gender
    self.size = size
    self.color = color
    self.price = price

shoes = [
  Shoe(
    'Air Jordan 1 High', 
    'Air Jordan', 
    'The One That Started It All', 
    "Men's Shoes",
    12, 
    'Black/Red/White', 
    '$170'
    ),
  Shoe(
    'Nike Air Max 90', 
    'Nike', 
    'Nothing as fly, nothing as comfortable, nothing as proven—the Air Max 90 adds spring to your step. With fun-loving details from the mushroom on the heel to the butterfly on the insole, it delivers sunny vibes. Plus, it lets you do good by looking good.', 
    "Men's Shoes",
    11,
    'Phantom/Iron Grey/Rush Pink/Celery',
    '$140'
    ),
  Shoe(
    "Nike Air Force 1 '07", 
    'Nike', 
    'Basic.', 
    "Women's Shoes",
    7,
    'White',
    '$100'
    )
]

def home(request):
  return HttpResponse('<h1>Hello World 👟</h1>')

def about(request):
  return render(request, 'about.html')

def shoes_index(request):
  return render(request, 'shoes/index.html', {
    'shoes': shoes
  })