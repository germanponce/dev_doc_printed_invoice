# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Doc Pre Printed Invoice Report',
    'version': '15.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Accounting',
    'description':
        """
        This Module add below functionality into odoo

        1.Allows you to print dynamically configured Invoice/Bill report\n

    """,
    'summary': 'Pre Printed Invoice Report',
    'author': 'Devintelle Consulting Service Pvt.Ltd & German Ponce D.',
    'website': 'http://www.devintellecs.com',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/print_invoice_config_views.xml',
        'views/account_invoice_views.xml',
        'report/template_dynamic_invoice_views.xml',
        'report/menu_dynamic_invoice_views.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: