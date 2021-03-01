from odoo import models, fields, api

class MaestroRamos(models.Model):

	_name = 'maestro.ramos'
	_description = 'Maestro de Ramos por Aseguradora'

	name = fields.Char(string = 'Ramos por Aseguradora')
	insurance_id = fields.Many2one('res.partner', string = 'Aseguradora')
	codigo = fields.Integer(string = 'Código del Ramo')
	iva = fields.Integer(string = 'Iva', help = 'Iva del ramo seleccionado')
	porcentaje_ramo = fields.Integer(string = 'Porcentaje')
	producto = fields.Char(string = 'producto')
	IdInsura = fields.Integer(string = 'Id Insura')
	IdSis = fields.Integer(string = 'Id Sis')
	team_id = fields.Many2one('crm.team', string = 'Canal de Ventas')
	insurer_id = fields.Integer(string = 'InsurerID')
	active = fields.Boolean(default=True)

class CrmLead(models.Model):
	
	_inherit = 'crm.lead'

	ramo_id = fields.Many2one('maestro.ramos', string = 'Ramo')
	iva_ramo = fields.Integer(string = 'Iva', help = 'Iva del ramo seleccionado')
	porcentaje_ramo = fields.Integer(string = 'Porcentaje', help = 'Porcentaje de comisión')
	numero_poliza = fields.Char(string = 'Número de Póliza')
	certificado = fields.Char(string = 'Número de Certificado')

	@api.onchange('ramo_id')
	def onchange_ramo(self):
		self.iva_ramo = self.ramo_id.iva 
		self.porcentaje_ramo = self.ramo_id.porcentaje_ramo 