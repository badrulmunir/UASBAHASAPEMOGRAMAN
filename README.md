# UASBAHASAPEMOGRAMAN
*Project UAS Bahasa Pemrograman*

NAMA    : BAdrul Munir
NIM     : 312210403 TI.22.A.4
STUDI   : TEKNIK INFORMATIKA
KELAS   : TI.22.A.4

## *DESKRIPSI*

1.	Buatlah 2 buah package, sebelumnya apasih package? Package adalah sekumpulan modul yang memiliki constructur init dalam satu folder atau bisa juga folder yang berisi sekumpulan file modul (.py), sedangkan modul adalah sebuah file yang berisikan sekumpulan kode fungsi dan global variabel yang disimpan dalam ekstensi .py.  Nah setelah tahu apa itu package dan modul diprogram kali ini kita akan membuat package model dan package view yang nanti kita akan isi modul disetiap package, ketentuannya seperti gambar dibawah ini.     

![image](https://user-images.githubusercontent.com/115614317/211723225-bdf963a2-356d-4372-8d66-5a7a1f95a966.png)  
•	File _init_.py berfungsi untuk membuat Python memperlakukan direktori yang berisi file sebagai paket atau secara singkat untuk merantai file-file yang terdapat di dalam package. 
•	File main.py berfungsi sebagai program utama yang akan di run oleh komputer. 
2.	Setelah kita membuat package dan modul selanjutnya kita akan membuat program CRUD 
(Create = Buat, Read = Baca, Update = Ubah, Delete = Hapus), karena semua file saling terhubung maka tidak ada ketentuan untuk membuat program awal, tapi disini kita akan membuat import pada file _init.py disetiap package agar nanti kita tidak perlu banyak menggunakan perintah import disetiap filenya nanti, hal ini sangat berguna diawal pembuatan program. Berikut adalah contoh source code program pada fiile __init_.py. 
sh  
# Pada file __init__.py di dalam package model 
from . daftar_nilai import * 
 
# Pada file __init__.py di dalam package view 
from .input_nilai import * 
from .view_nilai import * 


3.	Selanjutnya membuat program inputan user/pengguna pada file input_nilai.py, berikut contoh source code program pada file input_nilai.py. 

sh  
import model as m 
 def data_input(): 
        nama = str(input('NAMA\t\t: '))         
        nim = str(input('NIM\t\t: '))         
        uts = int(input('NILAI UTS\t: '))         
        uas = int(input('NILAI UAS\t: '))         
        tugas = int(input('NILAI TUGAS\t: '))         
        akhir = round(float((tugas * 0.3) + (uts * 0.35) + (uas * 0.35)), 
  

4.	Kemudian kita akan membuat program di dalam file daftar_nilai.py yang berisi modul perintah tambah_data(), ubah_data(), hapus_data() dan cari_data(). Berikut adalah contoh  source code programnya. 

sh 
import view 
 data = {}  def tambah_data():     
 print(f"{'TAMBAH DATA':^17}")     
 print('=' * 17)     
 view.data_input() 
 print('=' * 84)     
 print(f"|{'DATA BERHASIL DITAMBAHKAN':^82}|")     
 print('=' * 84) 
 def hapus_data(): 
    cari = str(input('MASUKAN NAMA: '))     
    if cari in data.keys(): 
        del data[cari]         
        print('=' * 84)         
        print(f"|{'DATA BERHASIL DIHAPUS':^82}|")         
        print('=' * 84) 
     else: 
        print('=' * 84)         
        print(f"|{'DATA TIDAK DITEMUKAN':^82}|")         
        print('=' * 84) 
 def ubah_data(): 
    cari = str(input('MASUKAN NAMA: '))     
    if cari in data.keys(): 
        print(f"{'UBAH DATA':^17}")         
        print('=' * 17)         
        view.data_input()         
        print('=' * 84)         
        print(f"|{'DATA BERHASIL DIUBAH':^82}|")         
        print('=' * 84) 
     else: 
        print('=' * 84)         
        print(f"|{'DATA TIDAK DITEMUKAN':^82}|")         
        print('=' * 84) 
 def cari_data(): 
    print(f"{'DATA PENCARIAN':^17}")     
    view.cetak_hasil_pencarian() 

        m.data[nama] = nama, nim, tugas, uts, uas, akhir         
        return nama, nim, tugas, uts, uas, akhir 


import view, berfungsi untuk menghubungkan atau mengambil modul yang ada di dalam file view agar nanti bisa terhubung atau digunakan. Disin kita juga membuat sebuah array bertipe data dictionary yang nanti berfungsi sebagai penyimpan data inputan user. Cara mengakses atau mengambil modul pada package view adalah dengan mengetik nama package titik lalu dilanjut nama modul yang ingin diambil berikut contoh syntaxnya: view.input_nilai(). 

5.	Lalu selanjutnya kita akan membuat program untuk menampilkan inputan yang tadi sudah kita buat pada file input_nilai.py, didalam file view_nilai.py kita akan membuat dua modul yaitu cetak_daftar_nilai(), dan cetak_hasil_pencarian() ada juga tambahan modul lainnya terserah kalian agar tampilan program terlihat lebih menarik. Berikut adalah contoh source code programnya. 

sh 
import model as d 
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
            print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}| " 
                    .format(a[1][0], a[1][1], a[1][2], a[1][3], a[1][4], a[1][5], no=n)) 
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
            print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}| " 
                .format(d.data[cari][0], d.data[cari][1],                  
                d.data[cari][2], 
d.data[cari][3],d.data[cari][4],d.data[cari][5], no=n))         
print('=' * 84)     
else: 
        print('=' * 84)         
        print(f"|{'DAFTAR DATA MAHASISWA':^82}|")         
        print('=' * 84)         
        print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")         
        print('=' * 84)         
        print(f"|{'DATA TIDAK DITEMUKAN':^82}|")         
        print('=' * 84) 
 def tampilan(): 
    print('=' * 84)     
    print(f"|{'Hasbi Assidiki':^82}|")     
    print(f"|{'PROGRAM INPUT DATA MAHASISWA':^82}|")     
    print('=' * 84) 
    
disini saya hanya menambahkan modul tampilan(), yakni tampilan awal program silahkan kalian berkreasi. 

6.	Setelah semua program telah kita buat didalam file-file yang sudah ditentukan programnya masing-masing selanjutnya kita akan buat program utamanya untuk menjalankan semua program yang kita buat tadi, ini lah fungsi dari file main.py yang sudah kita bahas diawal. 
Berikut contoh source code programnya. 
sh
import model 
import view 
import os 
view.tampilan() 
while True:     
print() 
    lanjut = str(input('    MENU\n==============\n(L) LIHAT\n(T) TAMBAH\n(U) UBAH\n(H) HAPUS\n(C) CARI\n(K) KELUAR\n==============\nPilihan : '))     
    os.system("cls")     
    if lanjut.lower() == 'l': 
        view.cetak_daftar_nilai() 
    elif lanjut.lower() == 't': 
        model.tambah_data()     
    elif lanjut.lower() == 'h': 
        model.hapus_data()    
    elif lanjut.lower() == 'u': 
        model.ubah_data()     
    elif lanjut.lower() == 'c': 
        model.cari_data()     
    elif lanjut.lower() == 'k': 
        break     
    else : 
        print('PILIH MENU YANG TERSEDIA') print('=' * 84) print(f"|{'KELUAR DARI PROGRAM':^82}|") print('=' * 84) 
 
pada file program kali ini kita meng-import semua package ager nantinya dapat kita panggil fungsi yang ada didalam package tersebut, dan juga kita mengimport os yang berfungsi untuk clearscreen pasti kalian sudah tahu dari fungsi import os tersebut. Kita juga menggunakan perulangan while agar nantinya bisa memproses perintah menu yang dipilih oleh user. Baik program kita sudah selesai disini saya akan menampilkan output programnya sebagai berikut.
