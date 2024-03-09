# -*- coding: utf-8 -*-
{
    'name': "Casa de Subastas",
    'summary': "Módulo creado para la casa de subastas",
    'description': """
        Este módulo ha sido creado para el proyecto final de SGE
    """,

    'icon_image':'static/description/icon.png',

    'author': "Marina Martín",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/subasta_security.xml',
        'security/ir.model.access.csv',
        'views/casa_subastas.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application":True,
    "installable":True
}

