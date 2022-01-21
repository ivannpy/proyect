import numpy as np
import string
from data_const import states


def get_curp(name, sur1, sur2, sex):
        if len(sur1[0:2].rstrip()) == 2:
            curp = sur1[0:2].rstrip() + sur2[0] + name[0]
        else:
            assert len(sur2[0:2].rstrip()) == 2
            curp = sur1[0].rstrip() + sur2[0:2].rstrip() + name[0]

        curp += f'{np.random.randint(low=0, high=99)}'.zfill(2)
        curp += f'{np.random.randint(low=1, high=12)}'.zfill(2)
        curp += f'{np.random.randint(low=1, high=31)}'.zfill(2)
        curp += sex + np.random.choice(states)[0]
        curp += "".join(list(np.random.choice(list(string.ascii_uppercase), size=4)))
        curp += "".join(list(np.random.choice(list(string.digits), size=2)))

        assert len(curp) == 18

        return curp



def get_curps(names, surnames1, surnames2, sex):
    curps = []

    for name, surname1, surname2, in zip(names, surnames1, surnames2):
        curp = get_curp(name, surname1, surname2, sex)
        curps.append(curp)

    return curps



def get_tels(n_size):
    nums = []
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
    rel_path = 'proyecto/data/photos/'
    paths_photos = []

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
    is_student = []
    is_academic = []
    is_worker = []

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
