# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CIIU(models.Model):
    _name = "ciiu" 

    name = fields.Char(
        string="Code and Description",
    )
