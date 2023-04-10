from django.db import models


# Create your model(s) here.
class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "CONTACT FORM"
        verbose_name_plural = "CONTACT FORMS"
