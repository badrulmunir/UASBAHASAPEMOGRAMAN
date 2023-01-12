import Model as m

def data_input():
    nama = str(input('NAMA\t\t: '))
    nim = str(input('NIM\t\t: '))
    uts = int(input('NILAI UTS\t: '))
    uas = int(input('NILAI UAS\t: '))
    tugas = int(input('NILAI TUGAS\t: '))
    akhir = round(float((tugas * 0.3) + (uts * 0.35) + (uas * 0.35)),
2)
    m.data[nama] = nama, nim, tugas, uts, uas, akhir
    return nama, nim, tugas, uts, uas, akhir