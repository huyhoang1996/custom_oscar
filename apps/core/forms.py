from django.forms import ModelForm
from models import *


class PlanForm(ModelForm):
    class Meta:
        model = Payment_Plan
        fields = ['name', 'description', 'price']