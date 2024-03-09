# -*- coding: utf-8 -*-
from odoo import models, fields, api

class subasta_pinturas(models.Model):
    _name = 'subastas.pinturas'
    _description = 'Pinturas'

    titulo = fields.Char('Titulo',size=30, required=True, help='Nombre de la Pintura')
    artista = fields.Many2one('subastas.artistas',ondelete='cascade',required=True)
    fecha = fields.Date(help='Fecha de creación')
    tecnica = fields.Selection([('acuarela','Acuarela'),('oleo','Óleo'),('aerografia','Aerografía'),('PinPas','Pintura al pastel'),('otro','Otro')], string='Técnica usada', default='acuarela')
    retrato = fields.Boolean(default=False,help='Es un retrato')
    foto = fields.Binary()


class subasta_artistas(models.Model):
    _name = 'subastas.artistas'
    _rec_name='nombre'
    _description = 'Artistas'

    nombre = fields.Char('Nombre',size=30,required=True,help='Nombre del Artista')
    fecha_nacimiento = fields.Date(help='Fecha de Nacimiento')
    lugar_nacimiento = fields.Char(help='Lugar de Nacimiento')    
    estilo_artistico = fields.Char(help='Estilo Artístico')
    biografia = fields.Text()