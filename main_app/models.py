from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

STATUS = (
    ('W', 'Wore Shoe'),
    ('N', "Not Worn"),
    ('P', 'Plan to wear'),
)

# Create your models here.
class Occasion(models.Model):
  name = models.CharField(max_length=50)
  activity = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('occasions_detail', kwargs={'pk': self.id})


class Shoe(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  gender = models.CharField(max_length=100)
  size = models.IntegerField()
  color = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  # add a M:M assoc between shoes & occasions
  occasions = models.ManyToManyField(Occasion)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'shoe_id': self.id})

  def wore_status(self):
    return self.wore_set.filter(date=date.today()).count() >= len(STATUS[0][0])

class Wore(models.Model):
  date = models.DateField('Shoe Status Date')
  status = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=STATUS,
    # set the default value for status to be 'O'
    default=STATUS[0][0]
  )

  # Create a shoe_id FK
  shoe = models.ForeignKey(
    Shoe, 
    on_delete=models.CASCADE
  )

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_status_display()} on {self.date}"
    # status used to be meal
    # might cause error

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for shoe_id: {self.shoe_id} @{self.url}"