# -*- coding: utf-8 -*-

from odoo import models, fields

class Ciiu(models.Model):
    _name = "res.ciiu"

    name = fields.Char(string="Code and Description")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")

class ResPArtner(models.Model):
    _inherit = 'res.partner'

    activity_id = fields.Many2one('res.ciiu', string='Actividad Ciiu')

