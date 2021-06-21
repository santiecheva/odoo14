from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    is_goodfather = fields.Boolean(string='Padrino')