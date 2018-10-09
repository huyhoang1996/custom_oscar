from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views import generic

from oscar.core.application import Application
from oscar.core.loading import get_class
from oscar.apps.customer.app import CustomerApplication as BaseCustomerApplication


class CustomerApplication(BaseCustomerApplication):

    def get_urls(self):
        urls = [
            # custom Profile
            url(r'^profile/$',
                login_required(self.profile_update_view.as_view()),
                name='profile-view'),

        ]
        urls += super(CustomerApplication, self).get_urls()
       
        return self.post_process_urls(urls)


application = CustomerApplication()
