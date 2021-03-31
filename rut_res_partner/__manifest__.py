# -*- coding: utf-8 -*-

{
    'name': "Formulario Contacto Reglas Colombianas",
    'version': '14.0.2.0.1',
    'summary': """Fórmulario para los negocios de cumplimiento""",
    'description': """Este módulo tiene los campos necesarios para guardar un contacto""",
    'author': "Santiago Echeverri Valencia",
    'company': "Rave Agencia de Seguros",
    'maintainer': 'Santiago Echeverri Valencia',
    'category': 'tools',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
        'views/ciiu.xml',
        'views/res_partner.xml',

        ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
}
