# -*- coding: utf-8 -*-

{
    'name': "Crm Cumplimiento",
    'version': '14.0.2.0.1',
    'summary': """Fórmulario para los negocios de cumplimiento""",
    'description': """Este módulo tiene los campos necesarios para tramitar una póliza de cumplimiento
                    por ejemplo, valor de contrato, asegurado, beneficiario""",
    'author': "Santiago Echeverri Valencia",
    'company': "Rave Agencia de Seguros",
    'maintainer': 'Santiago Echeverri Valencia',
    'category': 'sales',
    'depends': ['base','crm'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/crm_views.xml',
        'views/maestro_negocios.xml',
        ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
