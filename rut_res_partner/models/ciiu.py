from odoo import models, fields


class IndustrialClassification(models.Model):
    _name = "ciiu"  # res.co.ciiu
    _description = "ISIC List"

    name = fields.Char(
        string="Code and Description",
    )
    code = fields.Char('Code', required=True)
    description = fields.Char('Description', required=True)
 