from django.db import models
from phone_field import PhoneField

# Create your models here.
class BookingModel(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField()
    contact_number = PhoneField(blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
    