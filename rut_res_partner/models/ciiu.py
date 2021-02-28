from odoo import models, fields, api


class IndustrialClassification(models.Model):
    _name = "ciiu"  # res.co.ciiu
    _description = "ISIC List"

    name = fields.Char(
        string="Code and Description",
        compute="_compute_concat_name"
    )
    code = fields.Char('Code', required=True)
    description = fields.Char('Description', required=True)
 
    @api.onchange('code','description')
    def _compute_concat_name(self):
        for record in self:
            if record.code is False or record.description is False:
                record.name = ''
            else:
                record.name = str(record.code) + ' - ' + str(record.description)
