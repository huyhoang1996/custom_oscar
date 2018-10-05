from oscar.apps.dashboard.catalogue.tables import ProductTable as BaseProductTable
from oscar.core.loading import get_class, get_model
from django_tables2 import A, Column, LinkColumn, TemplateColumn
from django.utils.translation import gettext_lazy as _

DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Product = get_model('catalogue', 'Product')

class ProductTable(DashboardTable):
    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='dashboard/catalogue/product_row_image.html',
        orderable=False)
    
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='dashboard/catalogue/product_row_actions.html',
        orderable=False)

    icon = "sitemap"

    class Meta(DashboardTable.Meta):
        model = Product
        fields = ('title', 'date_updated')
        sequence = ('title', 'image', 'date_updated', 'actions')
        order_by = '-date_updated'