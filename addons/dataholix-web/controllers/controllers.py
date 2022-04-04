# -*- coding: utf-8 -*-
from odoo import http

class DataholixWeb(http.Controller):
    @http.route('/dataholix-web/dataholix-web/', auth='public')
    def index(self, **kw):
        return "Melih Omay test output"

    @http.route('/dataholix-web/customer/', auth='public')
    def customer(self, **kw):
        customers_orders = http.request.env['customer.order'].search([])
        output = "<h1>Customers Orders</h1><ul>"

        for customer in customers_orders:
            output += '<li>'+ customer['name'] + '</li>'

        output += "</ul>"
        return output

    @http.route('/dataholix-web/sales/', auth='public')
    def render_sale_order(self, **kw):
        try:
            leads = http.request.env['crm.lead'].search([])
        except Exception as e:
            return "can't Access =" + e.message

        output = "<h1>Sales Orders</h1><ul>"

        for lead in leads:
            output += '<li>Name:'+ lead['name'] + '</li>'

        output += "</ul>"
        return output

#     @http.route('/dataholix-web/dataholix-web/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dataholix-web.listing', {
#             'root': '/dataholix-web/dataholix-web',
#             'objects': http.request.env['dataholix-web.dataholix-web'].search([]),
#         })

#     @http.route('/dataholix-web/dataholix-web/objects/<model("dataholix-web.dataholix-web"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dataholix-web.object', {
#             'object': obj
#         })
