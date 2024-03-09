# -*- coding: utf-8 -*-
# from odoo import http


# class CasaSubastas(http.Controller):
#     @http.route('/casa_subastas/casa_subastas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/casa_subastas/casa_subastas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('casa_subastas.listing', {
#             'root': '/casa_subastas/casa_subastas',
#             'objects': http.request.env['casa_subastas.casa_subastas'].search([]),
#         })

#     @http.route('/casa_subastas/casa_subastas/objects/<model("casa_subastas.casa_subastas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('casa_subastas.object', {
#             'object': obj
#         })

