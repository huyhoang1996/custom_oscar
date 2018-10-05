from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView as BaseProductCreateUpdateView, ProductListView as BaseProductListView
from tables import ProductTable

class ProductCreateUpdateView(BaseProductCreateUpdateView):

    def __init__ (self):
       	self.formsets = {
            'image_formset': self.image_formset,
            'recommended_formset': self.recommendations_formset,
            'stockrecord_formset': self.stockrecord_formset
        }


class ProductListView(BaseProductListView):
	table_class = ProductTable
