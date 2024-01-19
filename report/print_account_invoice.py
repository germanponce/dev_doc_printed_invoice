# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import api, models


class account_invoice_report(models.AbstractModel):
    _name = 'report.dev_doc_printed_invoice.report_account_invoice_document'
        
    
    def convert(self, amount, cur):
        t = cur.amount_to_text(amount)
        t=t.replace("Cent", "HALALA")
        t= t.replace("Cents", "HALALA")
        t = t.replace('and','RIYALS AND')
        return t

    
    @api.multi
    def get_discount(self,obj):
        discount = 0
        for line in obj.invoice_line_ids:
            discount += (line.price_subtotal * line.discount) / 100
        return discount
            
    @api.multi
    def get_child(self,partner):
        for child in partner.child_ids:
            return child.name
        return ''
                
    @api.multi
    def get_address(self,partner):
        add = ''
        if partner:
            add = partner.street
            
        if partner.street2:
            if add:
                add = add + ', '+partner.street2
            else:
                add = partner.street2
        if partner.city:
            if add:
                add = add + ', '+partner.city
            else:
                add = partner.city
        return add        
            
    @api.multi
    def _get_lines(self,obj):
        f_lst =[]
        lst=[]
        i=0
        for line in obj.invoice_line_ids:
            i+=1
            lst.append({
                'code':line.product_id.default_code,
                'qty':line.quantity,
                'name':line.name,
                'price':line.price_unit,
                'total':line.price_subtotal, 
                'discount':line.discount,  
            })
            if i == obj.formate_id.num_of_line:
                i=0
                f_lst.append({'values':lst})
                lst=[]
                
        if lst:
            f_lst.append({'values':lst,})
        return f_lst

    @api.multi
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.invoice'].browse(docids)
        return {'doc_ids': docids,
                'doc_model': 'account.invoice',
                'docs': docs,
                'get_lines': self._get_lines,
                'convert': self.convert,
                'get_discount': self.get_discount,
                'get_child': self.get_child,
                'get_address': self.get_address
                }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
