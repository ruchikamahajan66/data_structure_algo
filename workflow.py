import subprocess

from ase.db import connect
from ase.io import write
import os

# db_file = 'exp_db/without_U/collect.db'
db_file = 'exp_db/with_U/collect.db'

# cif_directory = 'cif'
# json_directory = 'json'

# cif_directory = 'cif_without_U'
# json_directory = 'json_without_U'

cif_directory = 'cif_with_U'
json_directory = 'json_with_U'

def get_cif_data_from_ase_db():
    if not os.path.exists(cif_directory):
        os.makedirs(cif_directory)

    db = connect(db_file)

    for row in db.select():
        structure = row.toatoms()
        structure_id = row.id
        formula = row.formula
        cif_filename = os.path.join(cif_directory, f'{structure_id}_{formula}.cif')

        write(cif_filename, structure, format='cif')
        print(f'Saved structure {formula} as {cif_filename}')


def get_json_data_from_ase_db():
    if not os.path.exists(json_directory):
        os.makedirs(json_directory)

    db = connect(db_file)

    for row in db.select():
        structure = row.toatoms()
        structure_id = row.id
        formula = row.formula

        cif_filename = os.path.join(cif_directory, f'{structure_id}_{formula}.cif')

        json_filename = os.path.join(json_directory, f'{structure_id}_{formula}.json')
        command = 'ase convert ' + cif_filename + '  ' + json_filename
        subprocess.call(command, shell=True)
        write(json_filename, structure, format='cif')


if __name__ == '__main__':
    print(get_cif_data_from_ase_db())
    # print(get_json_data_from_ase_db())
