from odoo import api,Command, fields, models


class QuickDiagnosis(models.Model):
    _name = 'ona.quick.diagnosis'
    _description = 'Quick Diagnosis'

    name = fields.Char(
        string='Name',
        default="/",
        required=True,
        readonly=True,
        copy=False,
        index=True
    )

    sewer_id = fields.Many2one(
        comodel_name='ona.sewer',
        required=True,
        string='Sewer'
    )
    
    responsible = fields.Many2one(
        comodel_name='hr.employee',
        required=True,
        string='Responsible'
    )

    date = fields.Datetime(
        string='Date',
        default=fields.Datetime.now,
        readonly=True
    )

    vehicle_accessibility = fields.Selection(
        string='Vehicle Accessibility',
        required=True,
        selection=[
            ('nac', 'NAC'),
            ('vl', 'VL'),
            ('pl', 'PL')
        ]
    )

    traffic_density = fields.Selection(
        string='Traffic Density',
        required=True,
        selection=[
            ('null', 'Null'),
            ('rare', 'Rare'),
            ('medium', 'Medium'),
            ('dense', 'Dense'),
        ]
    )

    h2s_risk = fields.Boolean(
        string='H2S Risk',
    )

    road_condition = fields.Selection(
        string='Road Condition',
        required=True,
        selection=[
            ('bitumen', 'Bitumen'),
            ('ground', 'Ground'),
        ]
    )

    ground_nature = fields.Selection(
        string='Ground Nature',
        required=True,
        selection=[
            ('flat', 'Flat'),
            ('slope', 'Slope'),
            ('steep_slope', 'Steep Slope'),
        ]
    )

    ivp_rating = fields.Selection(
        string='IVP Rating',
        selection=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        ]
    )

    weather = fields.Selection(
        string='Weather',
        selection=[
            ('dry', 'Dry'),
            ('rain', 'Rain'),
            ('heavy_rain', 'Heavy Rain'),
        ]
    )

    trunk_ids = fields.One2many(
        comodel_name='ona.trunk',
        inverse_name='quick_diagnosis_id', 
        string='Trunks',
    )

    ladder = fields.Selection(
        string='Ladder',
        selection=[
            ('good_condition', 'Good Condition'),
            ('bad_condition', 'Bad Condition'),
            ('absent', 'Absent'),
            ],
        required=True,
    )

    decantation = fields.Boolean(
        string='Decantation',
        default=False
    )

    buffer_accessibility = fields.Selection(
        string='Accessibility',
        selection=[
            ('a', 'A'),
            ('nma', 'NMA'),
            ('nap', 'NAP'),
            ('nac', 'NAC'),
            ('pp', 'PP'),
            ('s_bati', 'S/BATI'),
            ],
        required=True
    )

    buffer_condition = fields.Selection(
        string='Condition',
        selection=[
            ('good', 'Good'),
            ('bad', 'Bad'),
            ('absent', 'Absent'),
            ],
        required=True
    )
    
    buffer_level = fields.Float(
        string='Level'
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
    
    trunk_count = fields.Integer(
        related='sewer_id.trunk_count',
    )
    
    cunette = fields.Boolean(
        related='sewer_id.cunette',
    )
    
    sewer_type = fields.Selection(
        related='sewer_id.type',
    )
    
    sewer_fill_rate = fields.Selection(
        string='Fill Rate',
        required=True,
        selection=[
            ('30', '30%'),
            ('50', '50%'),
            ('70', '70%'),
            ('100', '100%'),
        ],
    )
    
    sewer_depth = fields.Float(
        string='Depth'
    )
    
    sewer_deregistration_obstacle = fields.Boolean(
        string='Deregistration Obstacle'
    )
    
    @api.onchange('sewer_id')
    def _onchange_sewer_id(self):
        for qd in self:
            qd.trunk_ids = [Command.delete(trunk_id.id) for trunk_id in qd.trunk_ids]
    
    
    def action_get_trunk_ids(self):
        for rec in self:
            trunks = [Command.delete(trunk_id.id) for trunk_id in rec.trunk_ids]
            if rec.sewer_id:
                trunk_ids = rec.sewer_id.sewer_ids
                for trunk in trunk_ids:
                    trunks.append(Command.create(
                        {
                            'sewer_id': trunk.id,
                        }
                    ))
            rec.trunk_ids = trunks
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
                
    def action_confirm(self):
        for rec in self:
            if rec.name == "/":
                rec.name = self.env['ir.sequence'].next_by_code('ona.quick.diagnosis')
            rec.state = 'confirm'
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
            