from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import TemplateView, View

from portfolio.models import ContactForm


# Create your view(s) here.
class HomePageView(TemplateView):
    template_name = 'portfolio/index.html'


class ContactFormView(View):
    
    def post(self, request):
        form_content = request.POST
        data = {
            "first_name": form_content.get("first-name"),
            "last_name": form_content.get("last-name"),
            "email": form_content.get("email"),
            "subject": form_content.get("subject"),
            "message": form_content.get("message")
        }
        ContactForm.objects.create(**data)
        return HttpResponseRedirect(reverse('home'))
