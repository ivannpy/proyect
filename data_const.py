import os
import numpy as np

cur_path = os.getcwd()

filepath_raw = os.path.join(cur_path, 'data', 'raw_data')
filepath_datasets = os.path.join(cur_path, 'data', 'datasets')

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

facu_mail = {'Facultad de Arquitectura': 'arquitectura',
            'Facultad de Ciencias': 'ciencias',
            'Facultad de Ciencias Políticas y Sociales': 'polacas',
            'Facultad de Contaduría y Administración': 'fca',
            'Facultad de Derecho': 'derecho',
            'Facultad de Economía': 'economia',
            'Facultad de Filosofía y Letras': 'filosofia',
            'Facultad de Ingeniería': 'ingenieria',
            'Facultad de Medicina': 'medicina',
            'Facultad de Medicina Veterinaria y Zootecnia': 'mvz',
            'Facultad de Odontología': 'odontologia',
            'Facultad de Psicología': 'psicologia',
            'Facultad de Química': 'quimica',
            'Escuela Nacional de Trabajo Social': 'ents',
            'Escuela Nacional de Lenguas, Lingüística y Traducción': 'enallt',
            'Instituto de Investigaciones en Matemáticas Aplicadas y Sistemas': 'iimas'
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

uni_mail = {'Tienda UNAM': 'tienda',
            'TV UNAM': 'tv',
            'Archivo General': 'archivo',
            'Unidad de Posgrado': 'posgrado',
            'Museo Universitario de Arte Contemporáneo': 'muac',
            'Jardín Botánico IB-UNAM': 'botanico',
            'Universum': 'dgdc',
            'Medicina del Deporte': 'deporte',
            'Rectoría': 'dgp',
            'Estadio Olímpico': 'deporte',
            'CEPE': 'cepe',
            'Alberca': 'deporte',
            'Torre II de Humanidades': 'torre'
            }

uni_names = list(uni_mail.keys())


ins_mail = {'Instituto de Ciencias Nucleares': 'nucleares',
            'Instituto de Ingeniería': 'ii',
            'Instituto de Investigaciones en Matemáticas Aplicadas y Sistemas': 'iimas',
            'Instituto de Biolgía': 'biologicas',
            'Instituto de Química': 'quimica',
            'Instituto de Ciencias del Mar y Limnología': 'limnologia',
            'Instituto de Fisiología Celular': 'fisiologia',
            'Instituto de Geografía': 'geografia',
            'Instituto de Física': 'fisica',
            'Instituto de Investigaciones Jurídicas': 'juricas'
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
