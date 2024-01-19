# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

from odoo import models,fields, api
from odoo.exceptions import ValidationError


class InvoicePrintConfig(models.Model):
    _name ='invoice.print.config'

    name = fields.Char('Nombre', required="1")
    num_of_line = fields.Integer('No of Line Break',default=10,required="1")
    color=fields.Char('Color',default="#000",required="1")
    is_default = fields.Boolean('Establecer predeterminado')
    
    is_number = fields.Boolean('Número de impresión',default=True)
    num_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_number_bold = fields.Boolean('Negrita')
    number_m_top = fields.Float('Fuente superior',default=142)
    number_m_left = fields.Float('Fuente izquierda',default=90)
    
    is_partner = fields.Boolean('Print Partner',default=True)
    partner_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_partner_bold = fields.Boolean('Negrita')
    partner_m_top = fields.Float('Fuente superior',default=190)
    partner_m_left = fields.Float('Fuente izquierda',default=90)
    
    is_contact = fields.Boolean('Print Contact',default=True)
    contact_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_contact_bold = fields.Boolean('Negrita')
    contact_m_top = fields.Float('Fuente superior',default=190)
    contact_m_left = fields.Float('Fuente izquierda',default=90)
    
    is_address = fields.Boolean('Print Address',default=True)
    address_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_address_bold = fields.Boolean('Negrita')
    address_m_top = fields.Float('Fuente superior',default=190)
    address_m_left = fields.Float('Fuente izquierda',default=90)
    
    is_date = fields.Boolean('Print Date',default=True)
    date_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_date_bold = fields.Boolean('Negrita')
    date_m_top = fields.Float('Fuente superior',default=142)
    day_m_left = fields.Float('Day From Left',default=495)
    month_m_left = fields.Float('Month From Left',default=495)
    year_m_left = fields.Float('Year From Left',default=495)

    is_phone = fields.Boolean('Print Phone',default=True)
    phone_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_phone_bold = fields.Boolean('Negrita')
    phone_m_top = fields.Float('Fuente superior',default=224)
    phone_m_left = fields.Float('Fuente izquierda',default=90)

    is_line = fields.Boolean('Print Lines',default=True)
    line_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_line_bold = fields.Boolean('Negrita')
    line_m_top = fields.Float('Fuente superior',default=380)
    line_m_left = fields.Float('Fuente izquierda',default=0)
    
    code_width = fields.Char('Code Width',default='12%')
    qty_width = fields.Char('Qunatity Width',default='06%')
    name_width = fields.Char('Name Width',default='42%')
    price_width = fields.Char('Price Width',default='09%')
    total_width = fields.Char('Total Width',default='11%')
    discount_width = fields.Char('Discount Width',default='11%')

    is_untax = fields.Boolean('Print Untaxed Amount',default=True)
    untax_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_untax_bold = fields.Boolean('Negrita')
    untax_m_top = fields.Float('Fuente superior',default=1000)
    untax_m_left = fields.Float('Fuente izquierda',default=750)
    
    is_tax = fields.Boolean('Print Tax Amount',default=True)
    tax_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_tax_bold = fields.Boolean('Negrita')
    tax_m_top = fields.Float('Fuente superior',default=1000)
    tax_m_left = fields.Float('Fuente izquierda',default=750)
    
    is_total = fields.Boolean('Print Amount Total',default=True)
    total_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    is_total_bold = fields.Boolean('Negrita')
    total_m_top = fields.Float('Fuente superior',default=1000)
    total_m_left = fields.Float('Fuente izquierda',default=750)
    
    
    
    is_sales_man = fields.Boolean('Sales Man',default=True)
    sales_man_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    sales_man_bold = fields.Boolean('Negrita')
    sales_man_m_top = fields.Float('Fuente superior',default=1000)
    sales_man_m_left = fields.Float('Fuente izquierda',default=750)
    
    
    is_payment_term = fields.Boolean('Payment Terms',default=True)
    payment_term_font_size = fields.Float('Tamaño de fuente',default="13",required="1")
    payment_term_font_bold = fields.Boolean('Negrita')
    payment_term_m_top = fields.Float('Fuente superior',default=1000)
    payment_term_m_left = fields.Float('Fuente izquierda',default=750)
    
    @api.constrains('is_default')
    def _check_default(self):
        config_ids = self.search([('is_default','=',True)])
        if len(config_ids) > 1: 
            raise ValidationError("Solo puede existir un registro por defecto")
            
# vim:expandtab:smartindent:tabstop=4:4softtabstop=4:shiftwidth=4:
