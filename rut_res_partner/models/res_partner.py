# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

class CountryStateCity(models.Model):
    """
    Model added to manipulate  separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'
    _order = 'code'

    code = fields.Char(string = 'City Code', size=5, help='Code DANE - 5 digits-',
                       required=True)
    name = fields.Char('City Name', size=64, required=True)
    state_id = fields.Many2one('res.country.state', string = 'State', required=True)
    country_id = fields.Many2one('res.country', string ='Country', required=True)

class ResPartner(models.Model):

    _inherit = 'res.partner'

    _sql_constraints = [
    ('ident_unique',
        'UNIQUE(l10n_latam_identification_type_id,vat)',
        "¡El número de identificación debe ser único!"),
    ]


    city_id = fields.Many2one(
        comodel_name='res.country.state.city',
        string = "Municipio"
        )
    
    ciu_id = fields.Many2one(
        comodel_name='res.country.state.city',
        string = "Municipio"
        )

    city = fields.Char(related="city_id.name")

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


