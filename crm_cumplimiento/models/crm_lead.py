# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    insurance_id = fields.Many2one(
        'res.partner',
        string = 'Aseguradora',
        domain = "[('is_insurance','=',True)]",
        help = "Asigne la aseguradora que toma el negocio",
        index = True 
    )

    dcto_negocio = fields.Char(
        string = 'Documento Negocio',
         help="Acta 20394 Medellín"
        )

    valor_contrato = fields.Monetary(
        currency_field='company_currency', 
        string="Valor del Contrato",
        tracking=True,
        help="Digite el Valor total del contrato"
    )

    riesgo = fields.Integer(
        compute='_logica_riesgo',
        string = "Riesgo",
        store = True,
        default = 1
    )

    tipo_poliza_id = fields.Many2one('tipo.poliza', string = 'Tipo de Póliza', index=True)
    contrato_id = fields.Many2one('maestro.contratos', string = 'Tipo de Contrato' )
    subcontrato_id = fields.Many2one('maestro.subcontratos', string = 'Subtipo de Contrato', 
        domain = "[('contrato_id','=',contrato_id)]")
    objeto_contrato = fields.Html(string = 'Objeto del contrato')

    comentario = fields.Html(
        string="Comentario"
    )

    @api.depends('subcontrato_id')
    def _logica_riesgo(self):
        for record in self:
            if record.subcontrato_id:
                if 0 <=record.valor_asegurar < record.subcontrato_id.verde_hasta:
                    record.riesgo_id = 1
                elif record.subcontrato_id.verde_hasta <= record.valor_asegurar < record.subcontrato_id.amarillo_hasta:
                    record.riesgo_id = 3
                elif record.subcontrato_id.amarillo_hasta <= record.valor_asegurar < record.subcontrato_id.naranja_hasta:
                    record.riesgo_id = 7
                elif record.subcontrato_id.naranja_hasta <= record.valor_asegurar:
                    record.riesgo_id = 13
