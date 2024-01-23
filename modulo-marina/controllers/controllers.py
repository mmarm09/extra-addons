# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo-marina(http.Controller):
#     @http.route('/modulo-marina/modulo-marina', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo-marina/modulo-marina/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo-marina.listing', {
#             'root': '/modulo-marina/modulo-marina',
#             'objects': http.request.env['modulo-marina.modulo-marina'].search([]),
#         })

#     @http.route('/modulo-marina/modulo-marina/objects/<model("modulo-marina.modulo-marina"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo-marina.object', {
#             'object': obj
#         })

