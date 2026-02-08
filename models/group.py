# -*- coding: utf-8 -*-

from odoo import models, fields

class AccessGroup(models.Model):
    _name = 'access.group'
    _description = 'Groupe d\'accès simple pour contrôler les vues'
    _rec_name = 'name_get'
    
    # Groupe
    name = fields.Char('Nom du groupe', required=True, translate=True, help='Nom du groupe (ex: Équipe Sales)')
    code = fields.Char('Code', required=True, unique=True, help='Code unique (ex: sales_team)')
    description = fields.Text('Description', help='Description du groupe')
    is_active = fields.Boolean('Active', default=True, help='Si coché, ce groupe est disponible pour la configuration')
    
    # Contrôle d'accès aux vues (flexible)
    view_ids = fields.Many2many('ir.ui.view', 'Vues disponibles', help='Vues auxquelles ce groupe a accès')
    default_access_mode = fields.Selection([
        ('allow', 'Autoriser'),
        ('deny', 'Refuser')
    ], string='Mode d\'accès par défaut', default='allow', help='Mode d\'accès par défaut pour les utilisateurs non-membres')
    
    # Utilisateurs dans le groupe
    user_ids = fields.Many2many('res.users', 'Membres', domain=[('active', '=', True)], help='Utilisateurs dans ce groupe')
    
    @api.depends('name', 'code')
    def name_get(self):
        return self.name
