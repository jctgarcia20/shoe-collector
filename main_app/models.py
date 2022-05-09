from django.db import models
from django.urls import reverse

# Create your models here.
class Shoe(models.Model):
  # First define the attributes/fields
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  # Django will create inputs for a form
  # TextField will create a <textarea>
  description = models.TextField(max_length=250)
  gender = models.CharField(max_length=100)
  size = models.IntegerField()
  color = models.CharField(max_length=100)
  price = models.CharField(max_length=100)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'shoe_id': self.id})
