from django.forms import ModelForm
from .models import Bought

class BoughtForm(ModelForm):
  class Meta:
    model = Bought
    fields = ['date', 'status']