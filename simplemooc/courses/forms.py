from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template


class ContactCourse(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_email(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        send_mail_template(subject, 'courses/contact_email.html', context,
                           [settings.CONTACT_EMAIL], self.cleaned_data['email'])

