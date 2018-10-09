from oscar.apps.customer.models import *  # noqa isort:skip
from oscar.apps.customer.abstract_models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _



# class User(AbstractUser):
#     phone = models.CharField(
#         _('phone'), max_length=255, blank=True)

#     class Meta:
#         db_table = 'auth_user'

