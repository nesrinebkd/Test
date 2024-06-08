from odoo import api,fields, models

class productTemplate (models.Model):
    _inherit = "product.template",

    def _search_named_product_ids(self, operator, value):

        domain = ['|', '|', '|', ('default_code', operator, value), ('product_variant_ids.default_code', operator, value),('name', operator, value), ('barcode', operator, value)]
        products = self.search(domain)
        if not products:
            search_terms = value.split()
            for term in search_terms:
                domain = ['|', ('name', operator, term), ('default_code', operator, term)]
                products = self.search(domain)
                if products:
                    break
        return [('id', 'in', products.ids)]

    search_product_name = fields.Char(search='_search_named_product_ids', store=False)

