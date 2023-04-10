from django.contrib import admin

from portfolio.models import ContactForm


# Register your model(s) here.
class ContactFormAdmin(admin.ModelAdmin):
    date_hierarchy = "submitted_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


admin.site.register(ContactForm, ContactFormAdmin)
