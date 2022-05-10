from django.db import models
from django.urls import reverse
from datetime import date

STATUS = (
    ('O', 'Own Shoe'),
    ('D', "Don't Own"),
    ('P', 'Plan to Own')
)

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

  def own_status(self):
    return self.bought_set.filter(date=date.today()).count() > 0

class Bought(models.Model):
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