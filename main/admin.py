from django.contrib import admin
from .models import BookingModel

@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)
