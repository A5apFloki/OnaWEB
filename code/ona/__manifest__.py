# -*- coding: utf-8 -*-
{
    'name': "ona",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'hr', 'res_region'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/sewer.xml',
        'views/quick_diagnosis.xml',
        'views/drainage.xml',
        'views/trunk.xml',
        'views/menu.xml',
        'report/ona_drainage_report.xml'
    ],
}
