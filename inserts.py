import pandas as pd
import data_const as c
import os

"""
A través de este script se modelan los procesos de 
transcripción de datasets bien formados
a inserts sql, escritos en archivos.sql
"""
def main(dataset, table_name):
    """
    PARAMETERS
    ----------
    dataset : str
            Ruta del dataset
    table_name :str
            La tabla donde son requeridos los inserts
    """
    filename = os.path.join(c.filepath_sql, f'{table_name}.sql')
    file = open(filename, 'w')
    data = pd.read_csv(dataset)

    atr_names = str(tuple(data.columns.tolist())).replace("'", "")

    for i in data.index:
        attr = str(tuple(data.iloc[i].values))
        attr = attr.replace('False', "'False'")
        attr = attr.replace('True', "'True'")
        attr = attr.replace('nan', "NULL")
        sql_line = f'insert into {table_name} {atr_names} values {attr};'

        file.write(sql_line + '\n')

    file.close()


if __name__ == '__main__':
    files = [c.filepath_client,
             c.filepath_partner,
             c.filepath_vehicle,
             c.filepath_travel,
             c.filepath_infraction,
             c.filepath_board,
             c.filepath_schedule]

    names = ['cliente', 'socio', 'vehiculo', 'viaje', 'infraccion', 'abordar', 'programar']

    for file, name in zip(files, names):
        main(file, name)
