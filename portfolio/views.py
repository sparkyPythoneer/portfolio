from re import template
from django.views.generic import TemplateView


# Create your view(s) here.
class HomePageView(TemplateView):
    template_name = 'portfolio/index.html'
