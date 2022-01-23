import numpy as np
import string
import time
import datetime
import data_const as c


def get_names(data_m, data_f, data_s, n_data, seed):
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
            egreso.append('No aplica')

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
