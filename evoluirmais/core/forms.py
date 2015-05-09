# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from decouple import config

from evoluirmais.core.models import Subscription


class ContactForm(forms.Form):
    name = forms.CharField(label=u'Nome',
                           widget=forms.TextInput(
                               attrs={'placeholder': ''}))
    email = forms.EmailField(label=u'E-mail',
                             widget=forms.TextInput(
                                 attrs={'placeholder': ''}))
    message = forms.CharField(label=u'Mensagem',
                              widget=forms.Textarea(
                                  attrs={'placeholder': ''}))

    def send_mail(self):
        subject = u'Contato do site (%s)' % self.cleaned_data['name']
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }

        message = render_to_string('contact_mail.txt', context)
        message_html = render_to_string('contact_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     config('DEFAULT_FROM_EMAIL'),
                                     [config('DEFAULT_TO_EMAIL')])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        # fields = ['email']
        widgets = {'type': forms.HiddenInput()}

    def send_mail(self):
        if self.cleaned_data['type'] == 1:
            typename = 'Participante'
        else:
            typename = 'Organizador'

        subject = u'Inscrição do site (%s)' % self.cleaned_data['email']
        context = {
            'email': self.cleaned_data['email'],
            'type': typename,
        }

        message = render_to_string('subscription_mail.txt', context)
        message_html = render_to_string('subscription_mail.html', context)
        msg = EmailMultiAlternatives(subject, message,
                                     config('DEFAULT_FROM_EMAIL'),
                                     [config('DEFAULT_TO_EMAIL')])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
