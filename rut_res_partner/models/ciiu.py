# -*- coding: utf-8 -*-

from odoo import models, fields,


class CIIU(models.Model):
    _name = "ciiu"

    name = fields.Char(string="Code and Description")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")
