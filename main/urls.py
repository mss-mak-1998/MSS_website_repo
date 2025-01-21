from django.urls import path
from .views import (landing_page_view, 
                    home_page_view, 
                    thank_you_page_view, 
                    portfolio_view,
                    about_view,privacy_policy_view, terms_conditions_view,
                    BookConsultView)

app_name = 'main'

urlpatterns = [
    path('',landing_page_view, name="landing"),
    path('home/',home_page_view, name="home"),
    path('booking/', BookConsultView.as_view(), name ='booking'),
    
    path('portfolio/', portfolio_view, name ='portfolio'),
    path('about/', about_view, name ='about'),
    path ('thank_you_page/', thank_you_page_view, name ='thank_you_page'),
    path ('privacy_policy/', privacy_policy_view, name ='privacy_policy'),
    path ('terms_conditions/', terms_conditions_view, name ='terms_conditions'),
]
