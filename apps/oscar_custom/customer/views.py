from oscar.apps.customer.views import ProfileUpdateView 
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse, reverse_lazy
from oscar.apps.customer.views import ChangePasswordView


    
# custom profile
ProfileUpdateView.active_tab = 'profile-update'
ProfileUpdateView.success_url = reverse_lazy('customer:profile-update')

ChangePasswordView.active_tab = 'change-password'
