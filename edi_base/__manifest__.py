# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoo PS EDI Framework',
    'version': '0.1',
    'summary': '',
    'category': 'Tools',
    'description': """
Odoo PS EDI Framework
=====================
    """,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/edi_connection.xml',
        'views/edi_integration.xml',
        'views/edi_synchronization.xml',
        'data/connection.xml',
    ],
    'demo': [
        'demo/res_partner_demo.xml',    
    ],

    'hidden': True,
    'auto_install': False
}
