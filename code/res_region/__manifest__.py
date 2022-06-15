# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 SARL ARTEC-INT (<http://www.artec-int.com>).			  #
#    Author: SARL ARTEC-INT (<http://www.artec-int.com>)						  #
###################################################################################
{
    'name': 'Algeria - Regions',
    'version': '12.0.1.0.0',
    'description': """Regions of Algeria """,
    'summary': 'Regions of Algeria',
    'author': 'SARL ARTEC-INT Coding Segment',
    'company': 'SARL ARTEC-INT',
    'maintainer': 'SARL ARTEC-INT',
    'live_test_url': 'http://demo.artec-int.com/mawarid',	
    'website': 'http://www.artec-int.com/mawarid',
    'category': 'Localisation',
    'data': [
        'security/ir.model.access.csv',
        'data/wilaya.xml',
        'data/commune.xml',
        'views/res_commune.xml'
    ],
	'demo': [],	
    'images': ['static/description/icon.png'],	
    'qweb': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,	
}
