# -*- coding: utf-8 -*-
from odoo import models, fields, api

class compania_cinematografica(models.Model):
    #_name = 'res.partner' --no hace falta
    _inherit = 'res.partner'
    premiada = fields.Boolean(default=False)
    is_cine=fields.Boolean()

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
    foto = fields.Binary()
    categoria = fields.Many2one('videoclub.categoria',ondelete='cascade',required=True)
    compania = fields.Many2one('res.partner')

    #Se subvenciona el 30% de la película
    subvencionado = fields.Integer(compute='_valor_subvencion') #no inmediato, solo al guardar
    invertido = fields.Integer(compute='_valor_inversion') #queremos verlo de modo inmediato
    def _valor_subvencion(self):self.subvencionado=self.presupuesto*0.3
    @api.depends('presupuesto')
    def _valor_inversion(self):self.invertido=self.presupuesto*0.7

class videoclub_categoria(models.Model):
    #atributos
    _name = 'videoclub.categoria'
    _rec_name='nombre'
    _description = 'Categoría'
    #campos
    nombre = fields.Char('Nombre', required=True, help='Nombre de la categoría')