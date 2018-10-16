from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    DeleteView, DetailView, FormView, ListView, UpdateView)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django_tables2 import SingleTableView

from oscar.apps.customer.utils import normalise_email
from oscar.core.compat import get_user_model
from oscar.core.loading import get_class, get_classes, get_model
from oscar.views.generic import BulkEditMixin

User = get_user_model()
class UserDetailView(DetailView):
    def __init__(self):
    	print 'hoang'

    template_name = 'dashboard/users/detail.html'
    model = User
    context_object_name = 'customer'