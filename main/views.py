from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.core.mail import send_mail
from .models import BookingModel
from .forms import BookingModelForm

# Landing Page
def landing_page_view(request):
    return render(request, 'main/landing.html')

# Home Page
def home_page_view(request):
    return render(request, 'main/home.html')

# Consultation Booking Form
class BookConsultView(generic.CreateView):
    template_name = 'main/booking.html'
    form_class = BookingModelForm
    context_object_name = 'booking'
    
    def get_success_url(self):
        return reverse('main:thank_you_page')
    
    def form_valid(self, form):
        # Extract email from the form
        email = form.cleaned_data.get('email')

        # Send confirmation email
        send_mail(
            subject='Free Consult Booked',
            message="We have received your request for a free consult. Thank you for booking!",
            from_email="mss@gmail.com",
            recipient_list=[email],
            fail_silently=False
        )

        # Save the form and proceed
        return super(BookConsultView, self).form_valid(form)

     
    
#Portfolio view
def portfolio_view(request):
    return render(request, 'main/portfolio.html')

#About view
def about_view(request):
    return render(request, 'main/about.html')

#Thank you page view
def thank_you_page_view(request):
    return render(request, 'main/thank_you_page.html')

#Privacy Policy
def privacy_policy_view(request):
    context = {}
    return render(request, 'main/privacy_policy.html', context)

def terms_conditions_view(request):
    context = {}
    return render(request, 'main/terms_conditions.html', context)
