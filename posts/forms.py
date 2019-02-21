from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    subject = forms.CharField(
        label=_('Subject'),
        required=True,
        max_length=100
    )
    email = forms.EmailField(
        label=_('Your email'),
        required=True
    )
    message = forms.CharField(
        label=_('Message'),
        required=True,
        max_length=2000,
        widget=forms.Textarea
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def send_email(self):
        send_mail(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
