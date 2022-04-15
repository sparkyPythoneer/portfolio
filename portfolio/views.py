from decouple import Csv, config

from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import TemplateView, View


# Create your view(s) here.
class HomePageView(TemplateView):
    template_name = 'portfolio/index.html'


class ContactFormView(View):
    http_method_names = ['post']

    def post(self, request):
        if request.method == 'POST':
            first_name = request.POST.get('first-name')
            last_name = request.POST.get('last-name')
            email = request.POST.get('email')
            email_subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = config('EMAIL_HOST_USER', default='example@gmail.com')
            recipient_list = config(
                'SELF', default='example@gmail.com', cast=Csv())

            message_body = f'{first_name} {last_name}: {email}\n\n{message}'

        try:
            send_mail(
                email_subject,
                message_body,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('home'))
        except Exception as err:
            print(str(err))
