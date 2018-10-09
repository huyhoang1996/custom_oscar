from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as BaseProductCreateUpdateView, ProductListView as BaseProductListView
from tables import ProductTable
from oscar.apps.dashboard.catalogue.views import ProductCreateRedirectView as BaseProductCreateRedirectView
from django.urls import reverse



class ProductCreateUpdateView(BaseProductCreateUpdateView):

    def __init__ (self, *args, **kwargs):
    	super(ProductCreateUpdateView, self).__init__(*args, **kwargs)
       	self.formsets = {
            'image_formset': self.image_formset,
            'recommended_formset': self.recommendations_formset,
            'stockrecord_formset': self.stockrecord_formset
        }


class ProductListView(BaseProductListView):
	table_class = ProductTable


# cuatom button new product
class ProductCreateRedirectView(BaseProductCreateRedirectView):

    def get_redirect_url(self, **kwargs):
    	# copy to can change QueryDict 
    	self.request.GET = self.request.GET.copy()
    	self.request.GET['product_class'] = 1
        form = self.productclass_form_class(self.request.GET)
        if form.is_valid():
            product_class = form.cleaned_data['product_class']
            return self.get_product_create_url(product_class)

        else:
            return self.get_invalid_product_class_url()
