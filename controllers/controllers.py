# -*- coding: utf-8 -*-
# from odoo import http


# class Myicecat(http.Controller):
#     @http.route('/myicecat/myicecat/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myicecat/myicecat/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myicecat.listing', {
#             'root': '/myicecat/myicecat',
#             'objects': http.request.env['myicecat.myicecat'].search([]),
#         })

#     @http.route('/myicecat/myicecat/objects/<model("myicecat.myicecat"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myicecat.object', {
#             'object': obj
#         })
