# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 SARL ARTEC-INT (<http://www.artec-int.com>).			  #
#    Author: SARL ARTEC-INT (<http://www.artec-int.com>)						  #
###################################################################################

from odoo import fields, models, api


class ResCommune(models.Model):
    _name = 'res.commune'
    _descritpion = 'Commune'
    _order = 'name,id'

    code = fields.Char(
        string='Code Commune', size=2,
        help=u'Le code de la commune sur deux positions',
        required=True
    )
    state_id = fields.Many2one(
        'res.country.state',
        string='Wilaya',
        required=True
    )
    name = fields.Char(
        string='Commune',
        required=True,
        translate=True
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    commune_id = fields.Many2one(
        'res.commune',
        string='Commune'
    )


    @api.onchange('commune_id')
    def commune_id_change(self):
        for partner in self:
            partner.state_id = partner.commune_id.state_id.id
            partner.city = partner.commune_id.name
            partner.country_id = partner.commune_id.state_id.country_id.id
