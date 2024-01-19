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

    
    def get_discount(self,obj):
        discount = 0
        for line in obj.invoice_line_ids:
            discount += (line.price_subtotal * line.discount) / 100
        return discount
            
    def get_child(self,partner):
        for child in partner.child_ids:
            return child.name
        return ''
                
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

    # def _get_report_values(self, docids, data=None):
    #     docs = self.env['account.move'].browse(docids)
    #     return {'doc_ids': docids,
    #             'doc_model': 'account.move',
    #             'docs': docs,
    #             'get_lines': self._get_lines,
    #             'convert': self.convert,
    #             'get_discount': self.get_discount,
    #             'get_child': self.get_child,
    #             'get_address': self.get_address
    #             }

    @api.model
    def _get_report_values(self, docids, data=None):
        context = self._context
        print ("########## _get_report_values >>>>>>>>>>>> ")
        print ("########## context: ", context)
        print ("########## docids: ", docids)
        print ("########## data: ", data)
        context = self._context
        if not docids:
            payslip_ids = context.get('active_ids', [])
            docids = payslip_ids
        payslip_obj = self.env['hr.payslip']
        docs_br = payslip_obj.browse(docids)
        
        data_args = {
                        'doc_ids': docids,
                        'doc_model': 'account.move',
                        'docs': docs,
                        'get_lines': self._get_lines,
                        'convert': self.convert,
                        'get_discount': self.get_discount,
                        'get_child': self.get_child,
                        'get_address': self.get_address
                    }
        # return report_obj.render('payroll_list_report.report_payroll_list_tr', data_args)
        return data_args
 
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
