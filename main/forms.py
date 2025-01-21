from django import forms
from .models import BookingModel

class BookingModelForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Gopolang',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Makgothi',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': 'syd@gmail.com',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
        })
    )
    contact_number = forms.IntegerField(required = False,
        widget=forms.TextInput(attrs={
            'placeholder': '*Optional* Eg: (+27) 69 570 4580',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'A short description of what your business needs assistance with. E.g., "We need to get more people interested in our product."',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-blue-400'
        })
    )

    class Meta:
        model = BookingModel
        fields = ('first_name', 'last_name', 'email', 'contact_number', 'description')  # Exclude 'created_at'
