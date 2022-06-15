from typing_extensions import Required
from odoo import api,Command, fields, models

class DrainageLine(models.Model):
    _name = 'ona.drainage.line'
    _description = 'Drainage Line'
    
    name = fields.Char(
        string='Name',
        compute='_compute_name',
    )
    
    date = fields.Datetime(
        related='drainage_id.date'
    )
    
    address = fields.Char(
        string='Address',
        required=True,
    )

    ml_pipes = fields.Integer(
        string='Pipe',
    )

    nbr_sewers = fields.Integer(
        string='Sewers',
    )

    nbr_drains = fields.Integer(
        string='Drains',
    )

    ml_channels = fields.Integer(
        string='Channels',
    )

    mcube_aspiration = fields.Integer(
        string='Aspiration',
    )

    waste = fields.Selection(
        string='Waste', 
        selection=[
            ('1/4', '1/4'),
            ('1/2', '1/2'),
            ('1/3', '1/3'),
            ('1', '1'),
        ],
        default="1/4",
        required=True,
    )
    
    state = fields.Selection(
        string='Status', 
        selection=[
            ('draft', 'Draft'),
            ('unaccomplished', 'Unaccomplished'),
            ('accomplished', 'Accomplished'),
            ('cancel', 'Cancel'),
        ],
        default="draft",
        readonly=True
    )
    
    note = fields.Text(
        string='Note'
    )
    
    drainage_id = fields.Many2one(
        comodel_name='ona.drainage',
        string='Drainage',
    )
    
    @api.depends('address', 'drainage_id.name')
    def _compute_name(self):
        for rec in self:
            if rec.address and rec.drainage_id:
                rec.name = rec.drainage_id.name + ' : ' + rec.address
            else:
                rec.name = False
    
    def action_unaccomplished(self):
        for rec in self:
            rec.state = 'unaccomplished'
    
    def action_accomplished(self):
        for rec in self:
            rec.state = 'accomplished'
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

class Drainage(models.Model):
    _name = 'ona.drainage'
    _description = 'Drainage'

    name = fields.Char(
        string='Name',
        default="/",
        required=True,
        readonly=True,
        copy=False,
        index=True
    )
    
    date = fields.Datetime(
        string='Date',
        default=fields.Datetime.now,
        readonly=True
    )
    
    responsible = fields.Many2one(
        comodel_name='hr.employee',
        required=True,
        string='Responsible'
    )
    
    truck_license_plate = fields.Char(
        string='Truck License Plate',
    )
    
    type = fields.Selection(
        selection=[
            ('hydromechanical', 'Hydromechanical Cleaning'),
            ('manual', 'Manual Cleaning'),
            ('aspiration', 'Aspiration'),
        ],
        default='manual',
        required=True,
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
    
    drainage_line_ids = fields.One2many(
        comodel_name='ona.drainage.line',
        inverse_name='drainage_id',
        string="Drainage Lines",
    )
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
                
    def action_confirm(self):
        for rec in self:
            if rec.name == "/":
                rec.name = self.env['ir.sequence'].next_by_code('ona.drainage')
            rec.state = 'confirm'
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'