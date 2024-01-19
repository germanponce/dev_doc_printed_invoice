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
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class AccountInvoice(models.Model):
    _inherit ='account.move'

    @api.model
    def _default_formate(self):
        config_ids = self.env['invoice.print.config'].search([('is_default','=',True)],limit=1)
        return config_ids.id
    
    formate_id = fields.Many2one('invoice.print.config','Formato de Reporte',default=_default_formate)

    def get_move_browse(self):
        context = self._context
        return True

    def get_invoice_name(self):
        context = self._context
        print ("############ get_invoice_name >>>>>>>>> ")
        print ("############ context ", context)
        print ("############ self ", self)
        return "NO HAY"

    def print_invoice_dynamic(self):
        for rec in self:
            if not rec.formate_id:
                raise UserError("No se tiene selecionado un Formato.")
            [data] = rec.read()
            datas = {
                        'ids': [rec.id],
                        'model': 'account.move',
                        'docs': rec,
                        'form': data,
                        'record_ids': [rec.id],
                        'record_id': rec.id,

                    }

            # act = self.env.ref('fx_workflow_sale_city.report_ticket_surtidor_from_so').with_context(datas).report_action(sale, datas)
            # act['products_info'] = products_info
            # return act
            
            act = self.env.ref('dev_doc_printed_invoice.action_print_invoice_template').with_context(datas).report_action(rec, datas)
            return act

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: