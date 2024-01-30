# -*- coding: utf-8 -*-
{
    "name": "Videoclub",
    "version":"16.0",
    "author":"Marina Martín",
    "license":"AGPL-3",
    "website": "https://www.yourcompany.com",
    "category":"Tools",
    "depends":["base"],

    # always loaded
    'data': [
        'security/videoclub_security.xml',
        'security/ir.model.access.csv',
        'views/videoclub_marina.xml',
        'views/templates.xml',
    ],
    "application":True,
    "installable":True
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

