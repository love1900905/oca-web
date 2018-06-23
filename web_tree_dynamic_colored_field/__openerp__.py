# -*- coding: utf-8 -*-
# © 2015 Camptocamp SA, Damien Crier
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Colorize field in tree views',
    'summary': 'Allows you to dynamically color fields on tree views',
    'category': 'Hidden/Dependency',
    'version': '9.0.2.0.0',
    'depends': ['web'],
    'author': "Camptocamp,Therp BV,Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'website': 'https://github.com/OCA/web',
    'demo': [
        "demo/res_users.xml",
    ],
    'data': [
        'views/web_tree_dynamic_colored_field.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
}