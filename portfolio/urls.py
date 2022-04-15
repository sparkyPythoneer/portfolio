from django.urls import path

from .views import ContactFormView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact-me/', ContactFormView.as_view(), name='contact-me'),

]
