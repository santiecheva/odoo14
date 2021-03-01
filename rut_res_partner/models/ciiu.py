# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CIIU(models.Model):
    _name = "ciiu" 

    name = fields.Char(
        string="Code and Description",
    )
    code = fields.Char(string = 'Code', required=True)
    description = fields.Char(string ='Description', required=True)
    

    @api.onchange('code','description')
    def _compute_concat_name(self):
        for record in self:
            if record.code is False or record.description is False:
                record.name = ''
            else:
                record.name = str(record.code) + ' - ' + str(record.description)
  