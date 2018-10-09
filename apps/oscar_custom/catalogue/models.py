from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractProductCategory
from django.utils.translation import ugettext_lazy as _


class Product(AbstractProduct):
    plan = models.ManyToManyField('core.Payment_Plan', blank=True, verbose_name=_("Plan"))
    url_video = models.CharField(max_length=250)
    
# class ProductCategory(AbstractProductCategory): 
    
#     class Meta:
#         managed = False
#         auto_created = True

from oscar.apps.catalogue.models import *