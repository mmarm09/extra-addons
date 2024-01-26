# -*- coding: utf-8 -*-
# from odoo import http


# class VideoclubMarina(http.Controller):
#     @http.route('/videoclub_marina/videoclub_marina', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclub_marina/videoclub_marina/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclub_marina.listing', {
#             'root': '/videoclub_marina/videoclub_marina',
#             'objects': http.request.env['videoclub_marina.videoclub_marina'].search([]),
#         })

#     @http.route('/videoclub_marina/videoclub_marina/objects/<model("videoclub_marina.videoclub_marina"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclub_marina.object', {
#             'object': obj
#         })

