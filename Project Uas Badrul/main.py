import Model
import View
import os
View.tampilan()
while True:
 print()
 lanjut = str(input(' MENU\n==============\n(L) LIHAT\n(T)TAMBAH\n(U) UBAH\n(H) HAPUS\n(C) CARI\n(K) KELUAR\n==============\nPilihan : '))
 os.system("cls")
 if lanjut.lower() == 'l':
  View.cetak_daftar_nilai()
 elif lanjut.lower() == 't':
  Model.tambah_data()
 elif lanjut.lower() == 'h':
  Model.hapus_data()
 elif lanjut.lower() == 'u':
  Model.ubah_data()
 elif lanjut.lower() == 'c':
  Model.cari_data()
 elif lanjut.lower() == 'k' :

  break
 else :
  print('PILIH MENU YANG TERSEDIA')
  print('=' * 84)
  print(f"|{'KELUAR DARI PROGRAM':^82}|")
  print('=' * 84)
