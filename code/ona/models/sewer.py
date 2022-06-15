from email.policy import default
from odoo import api, Command, fields, models
from odoo.exceptions import UserError


class SewerLine(models.Model):
    _name = 'ona.sewer.line'
    _description = 'Sewer Parent/Child'

    sewer_parent_id = fields.Many2one(
        comodel_name='ona.sewer',
        string='Parent'
    )
    
    sewer_child_id = fields.Many2one(
        comodel_name='ona.sewer',
        string='Child'
    )


class Sewer(models.Model):
    _name = 'ona.sewer'
    _description = 'Sewer'

    name = fields.Char(
        string='Name',
        default="/",
        required=True,
        readonly=True,
        copy=False,
        index=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    date = fields.Date(
        string='Date',
        default=fields.Date.today(),
        readonly=True
    )
    

    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='State',
        domain=[('country_id', '=', 62)],
        required=True
    )

    commune_id = fields.Many2one(
        comodel_name='res.commune',
        string='Commune',
        required=True,
        domain="[('state_id', '=?', state_id)]"
    )
    
    address = fields.Char(
        string='Address',
    )

    area = fields.Char(
        string='Area',
    )

    longitude = fields.Float(
        string='Longitude',
    )
    
    latitude = fields.Float(
        string='Latitude',
    )

    diameter = fields.Float(
        string='Diameter',
    )

    type = fields.Selection(
        string='Type',
        selection=[
            ('road', 'Road'),
            ('sidewalk', 'Sidewalk'),
            ('terrain', 'Terrain'),
            ('other', 'Other'),
        ],
        required=True,
        default="road"
        )

    cunette = fields.Boolean(
        string='Cunette',
        default=False
    )

    note = fields.Text(
        string='Note'
    )
    
    
    state = fields.Selection(
        string='Status', 
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('cancel', 'Cancel'),
            ],
        default="draft",
        readonly=True
    )

    sewer_ids = fields.Many2many(
        comodel_name='ona.sewer',
        string='Trunks',
        domain="[('id', '!=', id), ('trunk_count', '<', 4)]",
        relation='sewer_sewer_rel',
        column1='linked_sewer_ids',
        column2='sewer_ids',
    )
    
    
    linked_sewer_ids = fields.Many2many(
        string='Linked Sewer',
        comodel_name='ona.sewer',
        relation='sewer_sewer_rel',
        column1='sewer_ids',
        column2='linked_sewer_ids',
    )
    
    
    trunk_count = fields.Integer(
        string='Trunk Count',
        compute='_compute_trunk_count',
        store=True
    )
    
    @api.depends('sewer_ids')
    def _compute_trunk_count(self):
        for rec in self:
            rec.trunk_count = len(rec.sewer_ids)
            
    @api.constrains('trunk_count')
    def _check_trunk_count(self):
        for rec in self:
            if rec.trunk_count > 4:
                raise UserError("You can't have more than 4 sewers")
    
    
    @api.constrains('sewer_ids')
    def _constrains_sewer_ids(self):
        for sewer in self:
            for s in sewer.sewer_ids:
                if sewer not in s.sewer_ids:
                    s.sewer_ids = [Command.link(sewer.id)]
            unlinked_sewers = self.env['ona.sewer'].search([('id', 'not in', sewer.sewer_ids.ids)])
            for us in unlinked_sewers:
                if sewer in us.sewer_ids:
                    us.sewer_ids = [Command.unlink(sewer.id)]
    
    

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            if rec.name == "/":
                rec.name = self.env['ir.sequence'].next_by_code('ona.sewer')
            rec.state = 'confirm'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'