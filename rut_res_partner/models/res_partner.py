# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CountryStateCity(models.Model):
    """
    Model added to manipulate  separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'
    _order = 'code'

    code = fields.Char(
        string = 'City Code',
        size=5, help='Code DANE - 5 digits-',
        required=True
        )
    name = fields.Char(
        'City Name',
        required=True
        )
    state_id = fields.Many2one(
        'res.country.state',
        string = 'State',
        required=True
        )
    country_id = fields.Many2one(
        'res.country',
        string ='Country',
        required=True
        )

class ResPartner(models.Model):

    _inherit = 'res.partner'

    firstName = fields.Char(string ="First Name")
    secondName = fields.Char(string ="Second Name")
    lastName = fields.Char(string ="Last Name")
    secondLastName = fields.Char(string ="Second Last Name")

    x_pn_retri = fields.Selection(
        [
            ("6", "Simplificado"),
            ("23", "Persona Natural"),
            ("7", "Común"),
            ("11", "Gran Autorretenedor Contribuyente"),
            ("22", "Internacional"),
            ("25", "Autorretenedor Común"),
            ("24", "Gran contribuidor")
        ],
        string ="Régimen"
    )

    _sql_constraints = [
    ('ident_unique',
        'UNIQUE(l10n_latam_identification_type_id,vat)',
        "¡El número de identificación debe ser único!"),
    ]


    @api.onchange('firstName', 'secondName', 'lastName', 'secondLastName', 'pos_name')
    def _concat_name(self):
        """
            This function concatenates the four name fields in order to be able to
            search for the entire name. On the other hand the original name field
            should not be editable anymore as the new name fields should fill it up
            automatically.
            @return: void
        """
        # Avoiding that "False" will be written into the name field
        if not self.firstName:
            self.firstName = ''

        if not self.secondName:
            self.secondName = ''

        if not self.lastName:
            self.lastName = ''

        if not self.secondLastName:
            self.secondLastName = ''

        # Collecting all names in a field that will be concatenated
        nameList = [
            self.firstName.encode(encoding='utf-8').strip(),
            self.secondName.encode(encoding='utf-8').strip(),
            self.lastName.encode(encoding='utf-8').strip(),
            self.secondLastName.encode(encoding='utf-8').strip()
        ]

        formatedList = []
        if self.companyName is False:
            if self.type == 'delivery':
                self.name = self.pos_name
                self.firstName = False
                self.secondName = False
                self.lastName = False
                self.secondLastName = False
            else:
                for item in nameList:
                    if item is not b'':
                        formatedList.append(item.decode('UTF-8'))
                    self.name = ' '.join(formatedList)


    @api.onchange('name')
    def on_change_name(self):
        """
        The name field gets concatenated by the four name fields.
        If a user enters a value anyway, the value will be deleted except first
        name has no value. Reason: In certain forms of odoo it is still
        possible to add value to the original name field. Therefore we have to
        ensure that this field can receive values unless we offer the four name
        fields.
        @return: void
        """
        if self.x_name1 is not False:
            if len(self.x_name1) > 0:
                self._concat_name()
