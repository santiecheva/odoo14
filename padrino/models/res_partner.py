# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = 'res.partner'

    godfather_id = fields.Many2one(
                                    'res.users',
                                    string= 'Padrino',
                                    domain="[('is_godfather','=',True)]"
                                )
