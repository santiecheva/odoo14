from odoo import models, fields

class MaestroContratos(models.Model):
	_name = 'maestro.contratos'

	name = fields.Char(string = 'Tipo de Contrato', index=True)


class MaestroSubContratos(models.Model):
	_name = 'maestro.subcontratos'

	name = fields.Char(string = 'Subcontrato', index=True)
	contrato_id = fields.Many2one('maestro.contratos',string = 'Contrato', required='True', index=True)
	verde_hasta = fields.Float(string='Verde hasta')
	amarillo_hasta = fields.Float(string='Amarillo hasta')
	naranja_hasta = fields.Float(string='Naranja hasta')
