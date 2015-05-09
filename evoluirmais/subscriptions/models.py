# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


TYPE_CHOICES = (
    (0, _(u'Participante')),
    (1, _(u'Organizador')),
)


class Subscription(models.Model):
    email = models.EmailField(_(u'Email'))
    type = models.IntegerField(_(u'Ordem no menu'), choices=TYPE_CHOICES,
                               default=0)
    created_at = models.DateTimeField(_(u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.email)

    class Meta:
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
