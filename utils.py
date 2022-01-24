import numpy as np
import pandas as pd
import string
import time
import datetime
from collections import Counter
import data_const as c


def get_names(data_m, data_f, data_s, n_data, seed=1):
    np.random.seed(seed)
    n_masc = int(np.random.normal(loc=(n_data)/2, scale=1))
    n_fem = n_data - n_masc
    card = [n_data, n_masc, n_fem]

    masc_names = list(data_m.loc[:, 'nombre'])
    fem_names = list(data_f.loc[:, 'nombre'])
    surnames = list(data_s.loc[:, 'apellido'])

    prob_masc = data_m.loc[:, 'frec']/data_m.loc[:, 'frec'].sum()
    prob_fem = data_f.loc[:, 'frec']/data_f.loc[:, 'frec'].sum()
    prob_ap1 = data_s.loc[:, 'frec_pri']/data_s.loc[:, 'frec_pri'].sum()
    prob_ap2 = data_s.loc[:, 'frec_seg']/data_s.loc[:, 'frec_seg'].sum()


    names_masc = list(np.random.choice(masc_names,
                                   n_masc,
                                   p=prob_masc))

    names_fem = list(np.random.choice(fem_names,
                                  n_fem,
                                  p=prob_fem))

    names = names_masc + names_fem

    surnames_1 = np.random.choice(surnames,
                              n_data,
                              p=prob_ap1)
    surnames_2 = np.random.choice(surnames,
                              n_data,
                              p=prob_ap2)

    return names, surnames_1, surnames_2, masc_names, fem_names, card



def get_curp(name, sur1, sur2, sex, socio=False):
    np.random.seed()

    if len(sur1[0:2].rstrip()) == 2:
        curp = sur1[0:2].rstrip() + sur2[0] + name[0]
        assert len(curp) == 4 and curp[3] == name[0]
    else:
        assert len(sur2[0:2].rstrip()) == 2
        curp = sur1[0].rstrip() + sur2[0:2].rstrip() + name[0]
        assert len(curp) == 4 and curp[3] == name[0]

    if socio:
        yy = f'{int(np.random.normal(loc=1980, scale=4, size=1)[0])}'[2:]
    else:
        p = np.random.choice(['stu', 'aca', 'wor'], 1, p=[0.7, 0.1, 0.2])
        if p[0] == 'stu':
            yy = f'{int(np.random.normal(loc=2003, scale=2, size=1)[0])}'[2:]
        elif p[0] == 'aca':
            yy = f'{int(np.random.normal(loc=1960, scale=4, size=1)[0])}'[2:]
        else:
            yy = f'{int(np.random.normal(loc=1980, scale=4, size=1)[0])}'[2:]

    curp += f'{yy}'.zfill(2)
    curp += f'{np.random.randint(low=1, high=12)}'.zfill(2)
    curp += f'{np.random.randint(low=1, high=31)}'.zfill(2)
    curp += sex + np.random.choice(c.states)[0]
    curp += "".join(list(np.random.choice(list(string.ascii_uppercase), size=4)))
    curp += "".join(list(np.random.choice(list(string.digits), size=2)))

    assert len(curp) == 18

    return curp



def get_curps(names, surnames1, surnames2, sex, socio=False):
    curps: list = []

    for name, surname1, surname2, in zip(names, surnames1, surnames2):
        curp = get_curp(name, surname1, surname2, sex, socio)
        curps.append(curp)

    return curps


def get_tels(n_size):
    nums: list = []

    for i in range(0, n_size):
        p = np.random.choice([0, 1], size=1, p=[0.6, 0.4])
        if p == 0:
            tel = '55' + "".join(list(np.random.choice(list(string.digits), size=8)))
            nums.append(int(tel))
        else:
            tel = '56' + "".join(list(np.random.choice(list(string.digits), size=8)))
            nums.append(int(tel))

    return nums


def get_photos(curps):
    rel_path: str = 'proyecto/data/photos/'
    paths_photos: list = []

    for curp in curps:
        p = np.random.choice([0, 1], size=1, p=[0.5, 0.5])
        if p == 0:
            ext = '.png'
        else:
            ext = '.jpg'

        path_photo = str(rel_path) + 'photo_' + str(curp) + ext

        paths_photos.append(path_photo)

    return paths_photos


def get_unity(curps):
    is_student: list = []
    is_academic: list = []
    is_worker: list = []

    for curp in curps:
        year = curp[4:6]
        if year in ('95', '96', '97', '98', '99', '00','01', '02', '03', '04',
        '05', '06','07', '08', '09', '10', '11', '12'):

            student = True
            worker = False

            p = np.random.choice([0, 1], size=1, p=[0.8, 0.2])
            if p == 0:
                academic = False
            else:
                if year in ('95', '96', '97', '98', '99', '00', '01', '02',
                '03', '04'):
                    academic = True
                else:
                    academic = False

            is_student.append(int(student))
            is_academic.append(int(academic))
            is_worker.append(int(worker))

        if 12 < int(year) < 95:
            p = np.random.choice([0, 1], size=1, p=[0.2, 0.8])

            if p == 0:
                student = False
                academic = True
                worker = False
            else:
                student = False
                academic = False
                worker = True

            is_student.append(int(student))
            is_academic.append(int(academic))
            is_worker.append(int(worker))

    return is_student, is_academic, is_worker


def get_fac_ins_uni(es_alu, es_aca, es_tra):
    faculty: list = []
    institute: list = []
    unit: list = []
    msg: str = 'No aplica'

    for s, a, w in zip(es_alu, es_aca, es_tra):
        if s == 1: # Es estudiante
            fac = np.random.choice(c.facu_names, size=1, p=c.proba_facu)
            faculty.append(fac[0])
            if a == 1: # También es académico
                ins = np.random.choice(c.ins_names, size=1)
                institute.append(ins[0])
            elif a == 0: # No es académico
                institute.append(msg)

            assert w == 0 # No es trabajador
            unit.append(msg)
        else: # No es estudiante
            assert s == 0
            faculty.append(msg)

            if a == 1: # Es académico
                ins = np.random.choice(c.ins_names, size=1)
                institute.append(ins[0])
                if w == 1: # También es trabajador
                    uni = np.random.choice(c.uni_names, size=1)
                    unit.append(uni[0])
                else: # No es trabajador
                    assert w == 0
                    unit.append(msg)

            else: # No es académico
                assert a == 0

                institute.append(msg)
                uni = np.random.choice(c.uni_names, size=1)
                unit.append(uni[0])

    return faculty, institute, unit


def get_mails(names, sur_1, sur_2, curps, facs, insts, units):
    emails: list = []

    for name, sur1, sur2, curp, fac, inst, unit in zip(names, sur_1, sur_2, curps, facs, insts, units):
        email = name.split(' ')[0]
        p = np.random.choice(['s1', 's2'], size=1, p=[0.5, 0.5])[0]
        if p == 's1':
            email += sur1
        else:
            email += sur2
        email += str(curp[4:6])

        msg = 'No aplica'
        if fac != msg:
            email += '@' + c.facu_mail[fac] + '.unam.mx'
            emails.append(email.lower())

        elif fac == msg:
            if inst != msg:
                email += '@' + c.ins_mail[inst] + '.unam.mx'
                emails.append(email.lower())
            elif inst == msg:
                assert unit != 'No aplica'
                email += '@' + c.uni_mail[unit] + '.unam.mx'
                emails.append(email.lower())

    return emails

def get_simple_mail(names):
    emails: list = []

    for name in names:
        email = name.split(' ')[0]
        email += "".join(list(np.random.choice(list(string.digits), size=3)))

        p = np.random.choice(['hotmail', 'gmail', 'yahoo', 'outlook'], size=1, p=[0.2, 0.5, 0.1, 0.2])[0]

        email += "@" + str(p) + '.com'

        emails.append(email.lower())

    return emails


def get_rfc(curps):
    rfcs: list = []

    for curp in curps:
        rfc = curp[0:11]
        rfc += "".join(list(np.random.choice(list(string.ascii_uppercase), size=2)))
        rfc += "".join(list(np.random.choice(list(string.digits), size=1)))
        rfcs.append(rfc.upper())

    return rfcs


def get_date(lower=2000, upper=2022):
    yy = np.random.randint(lower, upper)
    mm = np.random.randint(1, 13)
    dd = np.random.randint(1, 32)
    # Años bisiestos, etc
    if mm == 2:
        if dd > 28:
            if yy % 4 == 0:
                dd = 29
            else:
                dd = 28

    # Fecha de ingreso
    if mm in (4, 6, 9, 11) and dd == 31:
        dd = 30

    date = datetime.date(yy, mm, dd)

    return date, yy, mm, dd


def compare_date(date1, date2):

    return date1 >= date2


def get_time():
    hh = np.random.randint(6, 23, size=1)[0]
    mm = np.random.randint(0, 59, size=1)[0]
    ss = np.random.randint(0, 59, size=1)[0]
    timer = datetime.time(hh,mm,ss)

    return timer


def get_in_out(n_socio):
    ingreso: list = []
    egreso: list = []

    p = np.random.choice(['activo', 'no_activo'], size=n_socio, p=[0.85, 0.15])
    for i in p:
        joined = get_date(lower=2010)
        ingreso.append(joined[0])

        if i == 'no_activo':
            exit = get_date(joined[1])
            while compare_date(joined[0], exit[0]):
                exit = get_date(joined[1])

            egreso.append(exit[0])
        else:
            egreso.append(np.nan)

    return ingreso, egreso


def get_due_cho(n_data):
    duenios: list = []

    choferes = np.random.choice([0,1], size=n_data, p=[0.2, 0.8])

    for ch in choferes:
        if ch == 0:
            duenios.append(1)
        else:
            p = np.random.choice([0,1], size=1, p=[0.9,0.1])[0]
            duenios.append(p)

    return choferes, duenios


def get_lic(choferes):
    licencias = []

    for ch in choferes:
        if ch == 1:
            lic = "".join(list(np.random.choice(list(string.ascii_uppercase), size=1)))
            lic += "".join(list(np.random.choice(list(string.digits), size=8)))
            licencias.append(lic)
        else:
            lic = 'No aplica'
            licencias.append(lic)

    return licencias

def get_duenios(owners, n_veh):
    duenios = []
    poss_owners = list(owners.copy())

    for i in range(0, n_veh):
        owner = np.random.choice(poss_owners, size=1)[0]
        duenios.append(owner)
        poss_owners.remove(owner)

        if len(poss_owners) == 0:
            poss_owners = list(owners.copy())

    return duenios

def get_vehicle_info(n_vehicle):
    marcas = list(c.data_vehicle['vehicles'].keys())
    tipos = c.data_vehicle['tipo']
    num_c = c.data_vehicle['num_cilindros']
    pasajeros = c.data_vehicle['pasajeros']
    puertas = c.data_vehicle['puertas']
    combustibles = c.data_vehicle['combustible']

    marcas_, modelos_, anios_ = [], [], []
    tipos_, cils_, pasajeros_, = [], [], []
    puertas_, combs_, refac_ = [], [], []

    for n in range(n_vehicle):
        marca = np.random.choice(marcas, size=1, p=[0.3, 0.2, 0.5])[0]

        poss_mod = c.data_vehicle['vehicles'][marca]['modelos']
        poss_an = c.data_vehicle['vehicles'][marca]['años']

        modelo = np.random.choice(poss_mod, size=1, p=[0.6, 0.2, 0.2])[0]
        anio = np.random.choice(poss_an, size=1)[0]
        tipo = np.random.choice(tipos, size=1, p=[0.4, 0.6])[0]
        n_cil = np.random.choice(num_c, size=1, p=[0.7, 0.3])[0]
        max_pas = np.random.choice(pasajeros, size=1, p=[0.3, 0.7])[0]
        n_puertas = np.random.choice(puertas, size=1, p=[0.4, 0.6])[0]
        comb = np.random.choice(combustibles, size=1)[0]
        ref = np.random.choice([True, False], size=1, p=[0.8,0.2])[0]

        marcas_.append(marca)
        modelos_.append(modelo)
        anios_.append(anio)
        tipos_.append(tipo)
        cils_.append(n_cil)
        pasajeros_.append(max_pas)
        puertas_.append(n_puertas)
        combs_.append(comb)
        refac_.append(ref)

    return marcas_, modelos_, anios_, tipos_, cils_, pasajeros_, puertas_, combs_, refac_


def get_aseg_info(n_vehicle):
    vigencias = []

    aseg = c.aseguradoras_info['aseguradoras']
    tipos = c.aseguradoras_info['tipos_seguros']


    aseguradoras = np.random.choice(aseg, size=n_vehicle, p=[0.1, 0.5, 0.1, 0.1, 0.2])
    tipos_seguros = np.random.choice(tipos, size=n_vehicle, p=[0.6, 0.20, 0.1, 0.1])

    for n in range(n_vehicle):
        vig = get_date(lower=2021, upper=2023)[0]
        vigencias.append(vig)

    return aseguradoras, tipos_seguros, vigencias


def get_raz(n_vehicle):
    activos = np.random.choice([True, False], size=n_vehicle, p=[0.9,0.1])
    razones = []

    for act in activos:
        if act:
            razones.append('No aplica')
        else:
            razon = np.random.choice(c.razones_baja, size=1, p=[0.2, 0.3, 0.2, 0.2, 0.1])[0]
            razones.append(razon)

    return activos, razones

def get_dist_time(n_travel):
    distances = []
    times = []

    for n in range(n_travel):
        type = np.random.choice(['corto', 'largo'], size=1, p=[0.7, 0.3])[0]
        if type == 'corto':
            distance = abs(2 + np.random.normal(loc=0, scale=1))
            time = abs(10 + np.random.normal(loc=0, scale=2))
            distances.append(round(distance,2))
            times.append(int(time))
        else:
            distance = abs(10 + np.random.normal(loc=0, scale=4))
            time = abs(45 + np.random.normal(loc=0, scale=4))
            distances.append(round(distance,2))
            times.append(int(time))

    return distances, times


def get_infrac(travels, n_infrac):
    ids_socios = []
    num_ecos = []
    fechas = []

    data = travels[['id_socio', 'num_economico', 'fecha']]
    infractores = np.random.choice(data['id_socio'].unique(), size=10)

    for n in range(n_infrac):
        infractor = np.random.choice(infractores, size=1)[0]
        idx = data.index[data['id_socio'] == infractor].tolist()[0]
        num_eco = data.iloc[idx]['num_economico']
        fecha = data.iloc[idx]['fecha']

        ids_socios.append(infractor)
        num_ecos.append(num_eco)
        fechas.append(fecha)

        data.drop(index=idx, inplace=True)

    return ids_socios, num_ecos, fechas


def get_infrac_place(n_data):
    places_ = {'cp': [66455],
    'alcaldia': ['Coyoacán'],
    'calle': ['Circuito escolar']}

    # Direcciones
    cdmx_data = pd.read_csv(c.filepath_raw + '/all_cdmx_data.csv')
    np.random.seed(12345)
    to_select = np.random.choice(np.arange(0, cdmx_data.index[-1]), size=100, replace=True)
    cdmx_places = cdmx_data.iloc[to_select]
    cdmx_places.astype({'cp': 'float32'})

    for i in range(len(cdmx_places['cp'])):
        places_['cp'].append(list(cdmx_places['cp'])[i])
        places_['alcaldia'].append(list(cdmx_places['alcaldia'])[i])
        places_['calle'].append(list(cdmx_places['calle_num'])[i])

    mun = []
    cp = []
    calle = []

    for i in range(n_data):
        np.random.seed(None)
        p = np.random.choice(['CU', 'CDMX'], size=1, p=[0.8, 0.2])[0]
        if p == 'CU':
            mun.append(places_['alcaldia'][0])
            cp.append(places_['cp'][0])
            calle.append(places_['calle'][0])
        else:
            j = np.random.randint(1,len(places_['cp']))
            mun.append(places_['alcaldia'][j])
            cp.append(places_['cp'][j])
            calle.append(places_['calle'][j])

    return mun, cp, calle


def get_abordaje(curps, ids_viajes):
    viajes_list = []
    curps_list = []

    curps_pool = curps.copy()
    for id_viaje in ids_viajes:
        n_viajeros = np.random.choice([1,2,3,4], size=1, p=[0.1, 0.4, 0.3, 0.2])[0]
        if len(curps_pool) < n_viajeros:
            curps_pool = curps.copy()
        to_select = np.random.choice(list(curps_pool.index.values), size=n_viajeros, replace=False)
        pasajeros = curps_pool.iloc[to_select]

        for pasajero in pasajeros:
            viajes_list.append(id_viaje)
            curps_list.append(pasajero)

        curps_pool.drop(to_select, inplace=True)
        curps_pool = curps_pool.reset_index(drop=True)

        if len(curps_pool) == 0:
            curps_pool = curps.copy()

    return curps_list, viajes_list



def get_origen_destino(abordar, cliente):
    origenes = []
    destinos = []

    ids_viajes = list(abordar['id_viaje'].unique())

    for id_viaje in ids_viajes:
        curps = list(abordar.loc[abordar['id_viaje'] == id_viaje]['curp'])
        p = np.random.choice([0,1], size=1, p=[0.6,0.4])[0]

        if p == 0: # de casas a CU
            for curp in curps:
                origen = cliente.loc[cliente['curp'] == curp]['calle_num'].values[0]
                origenes.append(origen)

                destino_1 = cliente.loc[cliente['curp'] == curp]['facultad'].values[0]
                destino_2 = cliente.loc[cliente['curp'] == curp]['instituto'].values[0]
                destino_3 = cliente.loc[cliente['curp'] == curp]['unidad'].values[0]
                for i in [destino_1, destino_2, destino_3]:
                    if i != 'No aplica':
                        destinos.append(i)
                        break
        else: # De CU a sus casas
            for curp in curps:
                origen_1 = cliente.loc[cliente['curp'] == curp]['facultad'].values[0]
                origen_2 = cliente.loc[cliente['curp'] == curp]['instituto'].values[0]
                origen_3 = cliente.loc[cliente['curp'] == curp]['unidad'].values[0]
                for i in [origen_1, origen_2, origen_3]:
                    if i != 'No aplica':
                        origenes.append(i)
                        break

                destino = cliente.loc[cliente['curp'] == curp]['calle_num'].values[0]
                destinos.append(destino)

    return origenes, destinos



def add_redondos(board, travel, client, partner, vehicle):
    # Par Programar
    curps_programar = []
    ids_viajes_programar = []
    h_entradas = []
    h_salidas = []
    redondos = []
    # Para Viaje
    ids_viajes_viaje = []
    ids_socios = []
    nums_ecos = []
    distancias = []
    tiempos = []
    fechas = []
    # Para Abordar
    curps_abordar = []
    ids_viajes_abordar = []
    origenes = []
    destinos = []

    # Clientes que van a programar viajes
    curps_to_sche = np.random.choice(client['curp'].unique().tolist(), size=50)
    last_travel = int(list(travel['id_viaje'])[-1].split('-')[1])

    for curp in curps_to_sche:
        n_to_sch = np.random.randint(1, 50, size=1)[0]

        hh_e = np.random.choice([7, 8], size=1, p=[0.6, 0.4])[0]
        hh_s = np.random.choice([13, 14, 15], size=1, p=[0.2, 0.4, 0.4])[0]
        h_entrada = datetime.time(hour=hh_e)
        h_salida = datetime.time(hour=hh_s)

        for n in range(n_to_sch):
            # Programar ida
            last_travel += 1
            id_viaje_ida = 'v-'+f'{last_travel}'.zfill(6)
            redondo = np.random.choice([True, False], size=1, p=[0.6, 0.4])[0]

            curps_programar.append(curp)
            ids_viajes_programar.append(id_viaje_ida)
            h_entradas.append(h_entrada)
            h_salidas.append(np.nan)

            redondos.append(redondo)

            # Viaje de Ida
            id_socio = np.random.choice(list(partner['id_socio']), size=1)[0]
            num_eco = np.random.choice(list(vehicle['num_economico']), size=1)[0]
            distancia = abs(2 + np.random.normal(loc=0, scale=1))
            tiempo = abs(10 + np.random.normal(loc=0, scale=2))
            fecha = get_date(lower=2021)[0]

            ids_viajes_viaje.append(id_viaje_ida)
            ids_socios.append(id_socio)
            nums_ecos.append(num_eco)
            distancias.append(round(distancia, 2))
            tiempos.append(int(tiempo))
            fechas.append(fecha)

            # Abordaje de ida
            origen = client.loc[client['curp'] == curp]['calle_num'].values[0]
            destino_1 = client.loc[client['curp'] == curp]['facultad'].values[0]
            destino_2 = client.loc[client['curp'] == curp]['instituto'].values[0]
            destino_3 = client.loc[client['curp'] == curp]['unidad'].values[0]
            for i in [destino_1, destino_2, destino_3]:
                if i != 'No aplica':
                    destino = i
                    break

            curps_abordar.append(curp)
            ids_viajes_abordar.append(id_viaje_ida)
            origenes.append(origen)
            destinos.append(destino)

            if redondo:
                last_travel += 1
                id_viaje_regreso = 'v-' + f'{last_travel}'.zfill(6)

                # Programar regreso
                curps_programar.append(curp)
                ids_viajes_programar.append(id_viaje_regreso)
                h_entradas.append(np.nan)
                h_salidas.append(h_salida)
                redondos.append(redondo)

                # Viaje de regreso
                id_socio = np.random.choice(list(partner['id_socio']), size=1)[0]
                num_eco = np.random.choice(list(vehicle['num_economico']), size=1)[0]
                distancia += np.random.normal(0, 0.01)
                tiempo += np.random.normal(0, 0.1)

                ids_viajes_viaje.append(id_viaje_regreso)
                ids_socios.append(id_socio)
                nums_ecos.append(num_eco)
                distancias.append(round(distancia, 2))
                tiempos.append(int(tiempo))
                fechas.append(fecha)

                # Abordaje de regreso
                curps_abordar.append(curp)
                ids_viajes_abordar.append(id_viaje_regreso)
                origenes.append(destino)
                destinos.append(origen)

    programar_ = [curps_programar, ids_viajes_programar, h_entradas, h_salidas, redondos]
    viaje_ = [ids_viajes_viaje, ids_socios, nums_ecos, distancias, tiempos, fechas]
    abordar_ = [curps_programar, ids_viajes_programar, origenes, destinos]

    return programar_, viaje_, abordar_
