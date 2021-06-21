from odoo import models, fields


class ResUsers(models.Model):

    _inherit = 'res.users'

    is_goodfather = fields.Boolean(string='Padrino') 