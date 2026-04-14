from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    party_size = models.SmallIntegerField(default=1)

    class Meta: 
        unique_together = ('reservation_date', 'reservation_slot')

    def clean(self):
        if self.reservation_date < timezone.now().date():
            raise ValidationError("Cannot book in the past")

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
