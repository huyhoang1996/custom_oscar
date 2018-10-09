from oscar.apps.dashboard.catalogue import forms as base_forms
from django import forms
from django.utils.translation import ugettext_lazy as _
from oscar.apps.catalogue.models import ProductCategory


class ProductForm(base_forms.ProductForm):

    class Meta(base_forms.ProductForm.Meta):

        fields = ['title', 'description', 'plan', 'categories']

    def save(self, commit=True):
        product = super(ProductForm, self).save(commit=False)
        if commit:
            product.save()
            initial_category = self.initial.get('categories', None)
            final_category = self.cleaned_data['categories']

            # when create product
            if not initial_category:
                for cate in final_category:
                    ProductCategory.objects.create(product = product, category = cate)
            else:
                # when update product
                for cate in final_category:
                    if cate not in initial_category:
                        ProductCategory.objects.create(product = product, category = cate)

                for cate in initial_category:
                    if cate not in final_category:
                        ProductCategory.objects.filter(product = product, category = cate).delete()

        return product


# custom search product
class ProductSearchForm(forms.Form):
    # upc = forms.CharField(max_length=16, required=False, label=_('UPC'))
    title = forms.CharField(
        max_length=255, required=False, label=_('Product title'))

    def clean(self):
        cleaned_data = super(ProductSearchForm, self).clean()
        # cleaned_data['upc'] = cleaned_data['upc'].strip()
        cleaned_data['title'] = cleaned_data['title'].strip()
        return cleaned_data
