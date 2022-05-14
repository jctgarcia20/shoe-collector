from django.forms import ModelForm
from .models import Wore

class WoreForm(ModelForm):
  class Meta:
    model = Wore
    fields = ['date', 'status']