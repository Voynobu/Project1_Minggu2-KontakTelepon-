import os
from ModulKontak import*

os.system('cls')
print("=======Kontak=======")
print("1. DAFTAR KONTAK")
print("2. TAMBAH KONTAK")
Opsi = input("\nPilih opsi: ")
if(Opsi == "Tambah"):
    Tambah = True
    while(Tambah == True):
        NamaNew = input("Masukan nama kontak baru: ")
        NomorNew = input("Masukan nomor kontak baru: ")
        Verifikasi = input("Apakah informasi yang dimasukkan sudah benar? ")
        if (Verifikasi == "Ya"):
            Tambah = False
    TambahKontak(NamaNew, NomorNew)      
elif(Opsi == "Daftar"):
    DaftarKontak()
else:
    print("input tidak valid")



    
