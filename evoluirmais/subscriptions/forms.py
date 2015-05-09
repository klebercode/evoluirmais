# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from evoluirmais.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email')

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email'):
            raise ValidationError(_(u'Informe seu e-mail.'))

        return self.cleaned_data

    def send_mail(self, pk):
        subject = u'Evoluir Mais, inscrição realizada.'
        context = {
            'email': self.cleaned_data['email'],
            'subscription': pk,
        }

        email_to = self.cleaned_data['email']
        message = render_to_string('subscriptions/subscribe_mail.txt', context)
        message_html = render_to_string('subscriptions/subscribe_mail.html',
                                        context)
        msg = EmailMultiAlternatives(subject, message,
                                     'contato@evoluirmais.com.br',
                                     [email_to])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
