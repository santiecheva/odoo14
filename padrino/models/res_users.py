from odoo import models, fields


class ResUsers(models.Model):

    _inherit = 'res.users'

    is_godfather = fields.Boolean('Padrino', default=False)