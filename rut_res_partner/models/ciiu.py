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
    type = fields.Char(
        string = 'Tipo',
        compute="_compute_set_type"
    )
    has_parent = fields.Boolean(string='Has Parent?')
    parent = fields.Many2one('ciiu', string='Parent')

    has_division = fields.Boolean(string='Has Division?')
    division = fields.Many2one('ciiu',string= 'Division')

    has_section = fields.Boolean(string= 'Has Section?')
    section = fields.Many2one('ciiu',string= 'Section')

    hierarchy = fields.Selection(
        [
            (1, 'Has Parent?'),
            (2, 'Has Division?'),
            (3, 'Has Section?')
        ],
       string= 'Hierarchy'
    )


    @api.multi
    @api.depends('code', 'description')
    def _compute_concat_name(self):
        """
        This function concatinates two fields in order to be able to search
        for CIIU as number or string
        @return: void
        """
        for rec in self:
            if rec.code is False or rec.description is False:
                rec.name = ''
            else:
                rec.name = str(rec.code.encode('utf-8').strip()) + \
                    ' - ' + str(rec.description.encode('utf-8').strip())


    @api.multi
    @api.depends('has_parent')
    def _compute_set_type(self):
        """
        Section, Division and Parent should be visually separated in the tree
        view. Therefore we tag them accordingly as 'view' or 'other'
        @return: void
        """
        for rec in self:
            # Child
            if rec.has_parent is True:
                if rec.division is True:
                    rec.type = 'view'
                elif rec.section is True:
                    rec.type = 'view'
                else:
                    rec.type = 'other'
            # Division
            else:
                rec.type = 'view'
