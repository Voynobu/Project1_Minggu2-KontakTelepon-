import os
import time
import keyboard
from ModulKontak import*

while 1:
    os.system("cls")
    print("==========Kontak==========")
    print("1. Lihat Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan: ").strip() 
    if pilihan == "1":
        while 1:
            os.system("cls")
            TampilKontak()
            print("Tekan esc untuk kembali")
            while not keyboard.is_pressed("esc"):
                pass
            break 
               
    elif pilihan == "2":
            os.system("cls")
            nama = input("Nama : ")
            nomor = input("Nomor : ")
            TambahKontak(nama, nomor)
            print("Data berhasil dimasukkan")
            time.sleep(1)
            
    elif pilihan == "3":
        while 1:
            os.system("cls")
            nama = input("Nama : ")
            CariKontak(nama)
            print("Tekan esc untuk kembali")
            while not keyboard.is_pressed("esc"):
                pass
            break 
                
    elif pilihan == "4":
         os.system("cls")
         nama = input("Nama : ")
         HapusKontak(nama)
         time.sleep(1)

    elif pilihan == "5":
        break
