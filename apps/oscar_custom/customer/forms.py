from oscar.apps.customer.forms import UserForm as BaseUserForm

from django.utils.translation import gettext_lazy as _
from oscar.core.compat import (
    existing_user_fields, )


# Custom profile customer
class UserForm(BaseUserForm):

    class Meta(BaseUserForm.Meta):
        # check field in User model
        fields = existing_user_fields(['first_name','last_name', 'phone', 'email'])


"""
	if have model Profile, ProfileForm access Profile
	else access User 

"""
ProfileForm = UserForm


