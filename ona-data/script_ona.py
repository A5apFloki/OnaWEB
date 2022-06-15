from inspect import CO_VARKEYWORDS
import odoorpc
import os
import csv
import pandas as pd
import numpy as np

# login to odoo
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login('ona-db1', 'admin', 'admin')

# get sewer model
sewer = odoo.env['ona.sewer']

# open csv file
cwd = '%s/Desktop/ona/ona-data' % (os.getcwd())
file_path = '%s/regards.csv' % (cwd)
data = pd.read_csv(file_path, sep=';')

odoo_data = []
for i, row in data.iterrows():
    if 'annaba ville' in str(row.Rue).lower():
        odoo_row_data = {
            'name': row['ID'],
        }

        trunks = []
        for j in range(1, 5):
            trunk = row['c%s_ID' % (j)]
            if str(trunk) != 'nan' and trunk != ' ':
                trunks.append(trunk)
        odoo_row_data['sewer_ids'] = trunks

        odoo_data.append(odoo_row_data)
        

print(odoo_data)
