# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit ='account.invoice'

    @api.model
    def _default_formate(self):
        config_ids = self.env['invoice.print.config'].search([('is_default','=',True)],limit=1)
        return config_ids.id
    
    formate_id = fields.Many2one('invoice.print.config','Report Formate',default=_default_formate)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: