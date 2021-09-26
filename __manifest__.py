# -*- coding: utf-8 -*-
# bbi TK Testmodul Lagerhaltung

{
    'name': 'bbi Lagerhaltung',
    'version': '0.1',
    'category': 'Manufacturing/Lager',
    'depends': ['base'],
    'data': [
        'security/lager_security.xml',
        'security/ir.model.access.csv',
        'views/lager_kommiauftrag_view.xml',
        'views/lager_kommiauftragpos_view.xml',
        'views/lager_artikel_view.xml',
        'views/lager_menus.xml',
    ],
}
