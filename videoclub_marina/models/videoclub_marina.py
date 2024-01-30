# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    #atributos
    _name = 'videoclub.pelis'
    _description = 'Película'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de 12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    fechaestreno = fields.Date()

class videoclub_categoria(models.Model):
    #atributos
    _name = 'videoclub.categoria'
    _description = 'Categoría'
    #campos
    nombre = fields.Char('Nombre',required=True,help='Nombre de la categoría')
    #pelicula = fields.Many2one(
    #    'partner.delivery.zone',
    #    string='Delivery Zone',
    #    ondelete='cascade',
    #    required=True
    #)