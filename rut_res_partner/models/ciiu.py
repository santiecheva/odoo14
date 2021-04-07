# -*- coding: utf-8 -*-

from odoo import models, fields

class Ciiu(models.Model):
    _name = "res.ciiu"

    name = fields.Char(string="Code and Description")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")
