import os

cur_path = os.getcwd()

filepath_raw = os.path.join(cur_path, 'data', 'raw_data')
filepath_datasets = os.path.join(cur_path, 'data', 'datasets')

path_masc_names = os.path.join(filepath_raw, 'nombres_hombre.csv')
path_fem_names = os.path.join(filepath_raw, 'nombres_mujer.csv')
path_surnames = os.path.join(filepath_raw, 'apellidos.csv')

# Cardinalidades de las relaciones
cardinality = {'client': 10000,
               'partner': 150,
               'vehicle': 500,
               'travel': 25000,
               'infraction': 500,
               'board': 25000,
               'schedule': 5000
               }

# Datos para rellenar
states = ("Aguascalientes",
          "Baja California",
          "Baja California Sur",
          "Campeche",
          "Coahuila",
          "Colima",
          "Chiapas",
          "Chihuahua",
          "Durango",
          "Cuidad de México",
          "Guanajuato",
          "Guerrero",
          "Hidalgo",
          "Jalisco",
          "México",
          "Michoacán",
          "Morelos",
          "Nayarit",
          "Nuevo León",
          "Oaxaca",
          "Puebla",
          "Querétaro",
          "Quintana Roo",
          "San Luis Potosí",
          "Sinaloa",
          "Sonora",
          "Tabasco",
          "Tamaulipas",
          "Tlaxcala",
          "Veracruz",
          "Yucatán",
          "Zacatecas")

address = 'Cuidad de México'

# Filepaths
filepath_client = os.path.join(filepath_datasets, 'client.csv')
filepath_partner = os.path.join(filepath_datasets, 'partner.csv')
filepath_vehicle = os.path.join(filepath_datasets, 'vehicle.csv')
filepath_travel = os.path.join(filepath_datasets, 'travel.csv')
filepath_infraction = os.path.join(filepath_datasets, 'infraction.csv')
filepath_board = os.path.join(filepath_datasets, 'board.csv')
filepath_schedule = os.path.join(filepath_datasets, 'schedule.csv')

