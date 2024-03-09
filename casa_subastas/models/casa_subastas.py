# -*- coding: utf-8 -*-
from odoo import models, fields, api

# Modelo principal
class subasta_pinturas(models.Model):
    _name = 'subastas.pinturas'
    _rec_name='titulo'
    _description = 'Pinturas'

    titulo = fields.Char('Titulo',size=30, required=True, help='Nombre de la Pintura')
    # Campo Many2One para relacionar la pintura con el artista
    artista = fields.Many2one('subastas.artistas',ondelete='cascade',required=True)
    fecha = fields.Date(help='Fecha de creación')
    tecnica = fields.Selection([('acuarela','Acuarela'),('oleo','Óleo'),('aerografia','Aerografía'),('PinPas','Pintura al pastel'),('otro','Otro')], string='Técnica usada', default='acuarela')
    retrato = fields.Boolean(default=False,help='Es un retrato')
    foto = fields.Binary()

    precio_inicial=fields.Float()
    precio_final=fields.Float()

    # Campo calculado para la diferencia entre precio final y precio inicial
    diferencia_precios = fields.Float(compute='_valor_diferencia_precios')

    @api.depends('precio_inicial', 'precio_final')
    def _valor_diferencia_precios(self):
        for i in self:
            i.diferencia_precios = i.precio_final - i.precio_inicial

    # Campo heredado de res.partner
    compania = fields.Many2one('res.partner')


class subasta_artistas(models.Model):
    _name = 'subastas.artistas'
    _rec_name='nombre'
    _description = 'Artistas'

    nombre = fields.Char('Nombre',size=30,required=True,help='Nombre del Artista')
    fecha_nacimiento = fields.Date(help='Fecha de Nacimiento')
    lugar_nacimiento = fields.Char(help='Lugar de Nacimiento')    
    estilo_artistico = fields.Char(help='Estilo Artístico')
    biografia = fields.Text()


class subasta_subasta(models.Model):
    _name = 'subastas.subasta'
    _description = 'Subasta'

    nombre = fields.Char('Nombre',required=True,help='Nombre de la Subasta')
    # Campo Many2One para relacionar la pintura con la subasta
    pintura = fields.Many2one('subastas.pinturas',ondelete='cascade',required=True)
    fecha = fields.Date()
    

# Modelo a heredar
class compania_subasta(models.Model):
    #_name = 'res.partner' --no hace falta
    _inherit = 'res.partner'
    exito = fields.Boolean(default=False)
    is_subasta = fields.Boolean()