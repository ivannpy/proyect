"""
Diccionario correspondiente a cliente, 
donde las llaves son los atributos del cliente
y las listas son los valores asignados
"""
dict_to_df_cliente = {'curp': [],
                      'nombre': [],
                      'a_paterno': [],
                      'a_materno': [],
                      'calle_num': [],
                      'municipio': [],
                      'cp': [],
                      'colonia': [],
                      'estado': [],
                      'tel_casa': [],
                      'tel_celular': [],
                      'email': [],
                      'fotografia': [],
                      'facultad': [],
                      'instituto': [],
                      'unidad': [],
                      'es_alumno': [],
                      'es_academico': [],
                      'es_trabajador': []
                      }
"""
Diccionario correspondiente a socio,
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
dict_to_df_socio = {'id_socio': [],
                    'nombre': [],
                    'a_paterno': [],
                    'a_materno': [],
                    'rfc': [],
                    'num_licencia': [],
                    'calle_num': [],
                    'colonia': [],
                    'cp': [],
                    'municipio': [],
                    'estado': [],
                    'tel_celular': [],
                    'email': [],
                    'fotografia': [],
                    'ingreso': [],
                    'egreso': [],
                    'es_chofer': [],
                    'es_duenio': []
                    }

# Vehiculo
"""
Diccionario correspondiente a vehiculo,
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
dict_to_df_vehiculo = {'num_economico': [],
                       'id_socio': [],
                       'marca': [],
                       'modelo': [],
                       'anio': [],
                       'tipo_conduccion': [],
                       'num_cilindros': [],
                       'pasajeros': [],
                       'puertas': [],
                       'combustible': [],
                       'refaccion': [],
                       'aseguradora': [],
                       'tipo_seg': [],
                       'vigencia_seg': [],
                       'activo': [],
                       'razon': []
                       }
"""
Diccionario correspondiente a viaje,
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
dict_to_df_viaje = {'id_viaje': [],
                    'id_socio': [],
                    'num_economico': [],
                    'distancia': [],
                    'tiempo': [],
                    'fecha': []
                    }

"""
Diccionario correspondiente a infraccion,
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
dict_to_df_infraccion = {'id_infraccion': [],
                         'id_socio': [],
                         'num_economico': [],
                         'monto_pagar': [],
                         'agente': [],
                         'fecha': [],
                         'hora': [],
                         'municipio': [],
                         'cp': [],
                         'calle': []
                         }

"""
Diccionario correspondiente a abordar,
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
dict_to_df_abordar = {'curp': [],
                      'id_viaje': [],
                      'origen': [],
                      'destino': []
                      }
"""
Diccionario correspondiente a programar,
abordar y viaje(travel)
de forma homologa, los atributos son las 
llaves correspondientes y los valores 
corresponden a listas
"""
# Programar - Abordar - Travel
dict_to_df_programar = {'curp': [],
                        'id_viaje': [],
                        'h_entrada': [],
                        'h_salida': [],
                        'redondo': []
                        }
