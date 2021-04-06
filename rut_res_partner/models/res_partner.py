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
