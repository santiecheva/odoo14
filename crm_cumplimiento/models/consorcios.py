from odoo import models, fields, api, exceptions


class Consorcios(models.Model):

    _name = 'modelo.consorcio'
    _description = 'Consorcios'

    name = fields.Many2one(
        'res.partner',
        string='Asociado'
        )
    porcentaje = fields.Float(
        string='Porcentaje Participación'
        )
    Porcentaje_pago = fields.Float(
        string='Porcentaje Pago'
    )