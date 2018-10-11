from oscar.apps.customer.views import ProfileUpdateView 
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse, reverse_lazy
from oscar.apps.customer.views import ChangePasswordView


    
# custom profile
ProfileUpdateView.active_tab = 'profile-update'
ProfileUpdateView.success_url = reverse_lazy('customer:profile-update')

ChangePasswordView.active_tab = 'change-password'


# class ProfileUpdateView():
#     def __init__(self):
#         print '*************'
#         from oscar.core.loading import get_class, get_model, get_profile_class
#         Profile = get_profile_class()
#         print 'Profile ', Profile