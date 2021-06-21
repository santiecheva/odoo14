# -*- coding: utf-8 -*-

from odoo import models, fields, api


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

    tipo_poliza_id = fields.Many2one(
        'tipo.poliza',
        string = 'Tipo de Póliza',
        index=True
        )
    contrato_id = fields.Many2one(
        'maestro.contratos',
        string = 'Tipo de Contrato'
        )
    subcontrato_id = fields.Many2one(
        'maestro.subcontratos',
        string = 'Subtipo de Contrato',
        domain = "[('contrato_id','=',contrato_id)]"
        )
    objeto_contrato = fields.Text(
        string = 'Objeto del contrato'
    )

    comentario = fields.Html(
        string="Comentario"
    )

    ramo_id = fields.Many2one(
        'maestro.ramos',
        string='Ramo'
        )

    consorcio_ids = fields.Many2many(
        'modelo.consorcio',
        string='Seriedad'
        )

    consorcio_name = fields.Char(
    string='Nombre del consorcio'
    )

    tipo_consorcio = fields.Selection(
        [('ut','Unión Temporal'),('consorcio','Consorcio')],
        string='Tipo de consorcio'
    )

    beneficiario_id = fields.Many2one(
        'res.partner',
        string='Beneficiario'
        )

    @api.depends('subcontrato_id')
    def _logica_riesgo(self):
        for record in self:
            if record.subcontrato_id:
                if 0 <=record.valor_contrato < record.subcontrato_id.verde_hasta:
                    record.riesgo = 1
                elif record.subcontrato_id.verde_hasta <= record.valor_contrato < record.subcontrato_id.amarillo_hasta:
                    record.riesgo = 3
                elif record.subcontrato_id.amarillo_hasta <= record.valor_contrato < record.subcontrato_id.naranja_hasta:
                    record.riesgo = 7
                elif record.subcontrato_id.naranja_hasta <= record.valor_contrato:
                    record.riesgo = 13
