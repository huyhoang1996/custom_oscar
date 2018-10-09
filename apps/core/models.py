# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from oscar.apps.customer.abstract_models import AbstractUser

# Create your models here.
class DateTimeModel(models.Model):
    """
    Abstract model that is used for the model using created and modified fields
    """
    created = models.DateTimeField(_('Created Date'), auto_now_add=True,
                                   editable=False)
    modified = models.DateTimeField(
        _('Modified Date'), auto_now=True, editable=False)

    def __init__(self, *args, **kwargs):
        super(DateTimeModel, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Payment_Plan(DateTimeModel):

    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), max_length=255)
    price = models.IntegerField(_("Price"), default=0)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = _('Payment Plan')

class User(AbstractUser):

    phone = models.CharField(
        _('phone'), max_length=255, blank=True)
    plan = models.ForeignKey('Payment_Plan', related_name='user_plan_rel', on_delete=models.CASCADE, null=True, blank=True)
    # class Meta:
    #     db_table = 'auth_user'





