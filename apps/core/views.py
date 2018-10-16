# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.translation import ugettext_lazy as _
from forms import *
from django.contrib import messages
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
# Create your views here.
def home(request):
    try:
        # key_query is payment or movie
        """ Action render page notification timeout for user """
        return render(request, 'websites/home.html')
    except Exception, e:
        print "Error time out booking : ", e
        raise Exception(
            "ERROR : Internal Server Error .Please contact administrator.")


class PlanListView(ListView):
    template_name = 'websites/plan_list.html'
    context_object_name = 'classes'
    model = Payment_Plan

    def get_context_data(self, *args, **kwargs):
        ctx = super(PlanListView, self).get_context_data(*args, **kwargs)
        ctx['title'] = _("Payment Plan")
        return ctx

class PlanCreateView(CreateView):
    template_name = 'websites/plan_form.html'
    model = Payment_Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan')

    def get_context_data(self, **kwargs):
        ctx = super(PlanCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Add a new plan")
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Category created successfully"))
        return super(PlanCreateView, self).get_success_url()

class PlanUpdateView(UpdateView):
    template_name = 'websites/plan_form.html'
    model = Payment_Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan')

    def get_context_data(self, **kwargs):
        ctx = super(PlanUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Update category '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Category updated successfully"))
        return super(PlanUpdateView, self).get_success_url()