from django.contrib import admin
from .models import Shoe, Wore, Occasion

# Register your models here
admin.site.register(Shoe)
admin.site.register(Wore)
admin.site.register(Occasion)
