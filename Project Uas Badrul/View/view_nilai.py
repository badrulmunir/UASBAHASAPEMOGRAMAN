import Model as d

def cetak_daftar_nilai():
    if d.data.items():
        print('=' * 84)
        print(f"|{'DAFTAR DATA MAHASISWA':^82}|")
        print('=' * 84)
        print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
        print('=' * 84)
        n = 0
        for a in d.data.items():
            n += 1
            print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"

                .format(a[1][0], a[1][1], a[1][2], a[1][3], a[1][4],
a[1][5], no=n))
        print('=' * 84)
    else:
        print('=' * 84)
        print(f"|{'DAFTAR DATA MAHASISWA':^82}|")
        print('=' * 84)
        print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
        print('=' * 84)
        print(f"|{'TIDAK ADA DATA':^82}|")
        print('=' * 84)

def cetak_hasil_pencarian():
    cari = str(input('MASUKAN NAMA: '))
    if cari in d.data.keys():
        print('=' * 84)
        print(f"|{'DAFTAR DATA MAHASISWA':^82}|")
        print('=' * 84)
        print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
        print('=' * 84)
        n = 0
        for i in d.data.items():
            n += 1
            print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"

              .format(d.data[cari][0], d.data[cari][1],
                      d.data[cari][2],
    d.data[cari][3], d.data[cari][4], d.data[cari][5], no=n))
            print('=' * 84)
        else:
            print('=' * 84)
            print(f"|{'DAFTAR DATA MAHASISWA':^82}|")
            print('=' * 84)
            print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6} | {'UAS': ^ 6} | {'AKHIR': ^ 10} | ")
            print('=' * 84)
            print(f"|{'DATA TIDAK DITEMUKAN':^82}|")
            print('=' * 84)

def tampilan():
        print('=' * 84)
        print(f"|{'Badrul Munir':^82}|")
        print(f"|{'PROGRAM INPUT DATA MAHASISWA':^82}|")
        print('=' * 84)
