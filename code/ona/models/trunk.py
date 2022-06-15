from email.policy import default
from odoo import api, fields, models


class Trunk(models.Model):
    _name = 'ona.trunk'
    _description = 'Trunk'

    name = fields.Char(
        string='Name',
        compute='_compute_name',
    )
    original_sewer_id = fields.Many2one(
        related='quick_diagnosis_id.sewer_id'
    )

    sewer_id = fields.Many2one(
        comodel_name='ona.sewer',
        domain="[('id', '!=', original_sewer_id)]",
        readonly=True,
        # required=True,
        string='Sewer'
    )

    date = fields.Datetime(
        string='field_name',
        related='quick_diagnosis_id.date'
    )

    length = fields.Float(
        string='Length',
    )

    diameter = fields.Float(
        string='Diameter',
    )

    depth = fields.Float(
        string='Depth'
    )

    material = fields.Boolean(
        string='Material'
    )

    flow =  fields.Selection(
        string='Flow',
        required=True,
        selection=[
            ('dry', 'Dry'),
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('strong', 'Strong'),
        ],
        default='dry'
    )

    hydrocarbons_presence = fields.Boolean(
        string='Hydrocarbons Presence'
    )

    fill_rate = fields.Selection(
        string='Fill Rate',
        required=True,
        selection=[
            ('30', '30%'),
            ('50', '50%'),
            ('70', '70%'),
            ('100', '100%'),
        ],
        default='30'
    )

    deregistration_obstacle = fields.Boolean(
        string='Deregistration Obstacle'
    )

    deformation = fields.Boolean(
        string='Deformation'
    )

    crack = fields.Boolean(
        string='Crack'
    )

    rupture = fields.Boolean(
        string='Rupture'
    )

    partial_collapse_perforation = fields.Boolean(
        string='Partial Collapse Perforation'
    )

    total_collapse = fields.Boolean(
        string='Total Collapse'
    )

    visible_reinforcement = fields.Boolean(
        string='Visible Reinforcement'
    )

    branch_penetrating = fields.Boolean(
        string='Branch Penetrating'
    )

    sealing_gasket_appearing = fields.Boolean(
        string='Sealing Gasket Appearing'
    )

    longitudinal_dislocation = fields.Boolean(
        string='Longitudinal Dislocation'
    )

    vertical_dislocation = fields.Boolean(
        string='Vertical Dislocation'
    )

    transverse_dislocation = fields.Boolean(
        string='Transverse Dislocation'
    )

    direction_change = fields.Boolean(
        string='Direction Change'
    )

    roots = fields.Boolean(
        string='Roots'
    )

    infiltration = fields.Boolean(
        string='Infiltration'
    )

    degradation = fields.Boolean(
        string='Degradation'
    )

    note = fields.Text(
        string='Note'
    )

    state = fields.Selection([
           ('draft', 'Draft'),
           ('confirm', 'Confirm'),
           ('cancel', 'Cancel'),
       ], 
       string='Status', 
       default='draft'
    )

    quick_diagnosis_id = fields.Many2one(
        comodel_name='ona.quick.diagnosis',
        string='Quick Diagnosis'
    )
    
    
    @api.depends('quick_diagnosis_id','quick_diagnosis_id.sewer_id','sewer_id')
    def _compute_name(self):
        for rec in self:
            if rec.quick_diagnosis_id and rec.sewer_id:
                rec.name = rec.quick_diagnosis_id.sewer_id.name + ' <-----> ' + rec.sewer_id.name
            else:
                rec.name = False