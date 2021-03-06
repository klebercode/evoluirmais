# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


TYPE_CHOICES = (
    (1, _(u'Participante')),
    (2, _(u'Organizador')),
)


class Subscription(models.Model):
    email = models.EmailField(_(u'Email'))
    type = models.IntegerField(_(u'Tipo'), choices=TYPE_CHOICES, default=0)
    created_at = models.DateTimeField(_(u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
