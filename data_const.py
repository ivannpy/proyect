import os
import numpy as np

cur_path = os.getcwd()

filepath_raw = os.path.join(cur_path, 'data', 'raw_data')
filepath_datasets = os.path.join(cur_path, 'data', 'datasets')
filepath_sql = os.path.join(cur_path, 'sql_files', 'inserts')

# Filepaths de los csv para poblar
filepath_client = os.path.join(filepath_datasets, 'client.csv')
filepath_partner = os.path.join(filepath_datasets, 'partner.csv')
filepath_vehicle = os.path.join(filepath_datasets, 'vehicle.csv')
filepath_travel = os.path.join(filepath_datasets, 'travel.csv')
filepath_infraction = os.path.join(filepath_datasets, 'infraction.csv')
filepath_board = os.path.join(filepath_datasets, 'board.csv')
filepath_schedule = os.path.join(filepath_datasets, 'schedule.csv')

# Archivos csv con nombres
path_masc_names = os.path.join(filepath_raw, 'nombres_hombre.csv')
path_fem_names = os.path.join(filepath_raw, 'nombres_mujer.csv')
path_surnames = os.path.join(filepath_raw, 'apellidos.csv')

# Cardinalidades de las relaciones
cardinality = {'client': 10000,
               'partner': 200,
               'vehicle': 500,
               'travel': 25000,
               'infraction': 100,
               'board': 75000, # Se calcula on the fly
               'schedule': 5000 # Se calcula on the fly
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

facu_mail = {'Facultad de Arquitectura, CU': 'arquitectura',
            'Facultad de Ciencias, CU': 'ciencias',
            'Facultad de Ciencias Políticas y Sociales, CU': 'polacas',
            'Facultad de Contaduría y Administración, CU': 'fca',
            'Facultad de Derecho, CU': 'derecho',
            'Facultad de Economía, CU': 'economia',
            'Facultad de Filosofía y Letras, CU': 'filosofia',
            'Facultad de Ingeniería, CU': 'ingenieria',
            'Facultad de Medicina, CU': 'medicina',
            'Facultad de Medicina Veterinaria y Zootecnia, CU': 'mvz',
            'Facultad de Odontología, CU': 'odontologia',
            'Facultad de Psicología, CU': 'psicologia',
            'Facultad de Química, CU': 'quimica',
            'Escuela Nacional de Trabajo Social, CU': 'ents',
            'Escuela Nacional de Lenguas, Lingüística y Traducción, CU': 'enallt',
            'Instituto de Investigaciones en Matemáticas Aplicadas y Sistemas, CU': 'iimas'
            }

facu_names = list(facu_mail.keys())

proba_facu = [1/16,
        1/16 + 3/64,
        1/16,
        1/16 + 2/(16*3),
        1/16 + 6/64,
        1/16,
        1/(16*3),
        1/16,
        1/16,
        1/16,
        1/16,
        1/16,
        1/16,
        1/(16*4),
        1/(16*4),
        1/(16*4)]

uni_mail = {'Tienda UNAM, CU': 'tienda',
            'TV UNAM, CU': 'tv',
            'Archivo General, CU': 'archivo',
            'Unidad de Posgrado, CU': 'posgrado',
            'Museo Universitario de Arte Contemporáneo, CU': 'muac',
            'Jardín Botánico IB-UNAM, CU': 'botanico',
            'Universum, CU': 'dgdc',
            'Medicina del Deporte, CU': 'deporte',
            'Rectoría, CU': 'dgp',
            'Estadio Olímpico, CU': 'deporte',
            'CEPE, CU': 'cepe',
            'Alberca, CU': 'deporte',
            'Torre II de Humanidades, CU': 'torre'
            }

uni_names = list(uni_mail.keys())


ins_mail = {'Instituto de Ciencias Nucleares, CU': 'nucleares',
            'Instituto de Ingeniería, CU': 'ii',
            'Instituto de Investigaciones en Matemáticas Aplicadas y Sistemas, CU': 'iimas',
            'Instituto de Biolgía, CU': 'biologicas',
            'Instituto de Química, CU': 'quimica',
            'Instituto de Ciencias del Mar y Limnología, CU': 'limnologia',
            'Instituto de Fisiología Celular, CU': 'fisiologia',
            'Instituto de Geografía, CU': 'geografia',
            'Instituto de Física, CU': 'fisica',
            'Instituto de Investigaciones Jurídicas, CU': 'juricas'
            }

ins_names = list(ins_mail.keys())


marca_modelo = {'CHEVROLET': {'modelos': ['Aveo', 'Onix', 'Captiva'],
                               'años': np.arange(2010, 2021)},
                 'FORD': {'modelos': ['Figo', 'Fiesta', 'Sedán'],
                          'años': np.arange(2010, 2019)},
                 'NISSAN': {'modelos': ['Tsuru', 'Versa', 'Sentra'],
                            'años': np.arange(2000, 2016)}
                }


data_vehicle = {'vehicles': marca_modelo,
                'tipo': ['Cambio manual', 'Cambio automático'],
                'num_cilindros': [4, 6],
                'pasajeros': [3, 4],
                'puertas': [4, 5],
                'combustible': ['Motor gasolina', 'Motor diesel']
                }

aseguradoras_info = {'aseguradoras': ['AXA', 'BBVA', 'GNP', 'HDI', 'QUALITAS'],
                    'tipos_seguros': ['Básica', 'Limitada', 'Amplia', 'Plus']
                    }

razones_baja = ['Accidente', 'Baja voluntaria', 'Suspensión', 'Reporte de robo', 'Vehículo robado']
