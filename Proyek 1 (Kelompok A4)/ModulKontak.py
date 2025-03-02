import os
fileKontak = "daftarkontak.txt"

# Rangga Muhamad fajar
def TambahKontak(Nama, Nomor):
    template = f"{Nama}, {Nomor}\n"
    Buka = open("daftarkontak.txt","a")
    Buka.write(template)
    Buka.close()
    
# Zaidan Zulkaisi Setiaji
def TampilKontak():
    Buka = open("daftarkontak.txt", "r")
    print(Buka.read())
    Buka.close()

# Nauval Khairiyan
def MuatKontak():
    
    if not os.path.exists(fileKontak):
        return []
    with open(fileKontak, "r") as file:
        contacts = file.readlines()
    return [contact.strip().split(",") for contact in contacts]

def CariKontak(Nama):
    contacts = MuatKontak()
    hasil = []
    for contact in contacts:
        if Nama.lower() in contact[0].lower():
            hasil.append(contact)

    if hasil:
        print("\n Hasil Pencarian:")
        for contact in hasil:
            print(f"{contact[0]} - {contact[1]}")
    else:
        print("Kontak tidak ditemukan.")

# Dino Darmawan
def HapusKontak(NamaHapus):
    if not os.path.exists(fileKontak):
        print("Tidak ada kontak yang tersimpan")
        return
    with open(fileKontak, "r") as file:
        lines = file.readlines()
    with open(fileKontak, "w") as file:
        kontak_dihapus = False
        for line in lines:
            if NamaHapus.lower() not in line.lower():
                file.write(line)
            else:
                kontak_dihapus = True
    if kontak_dihapus:
        print(f"Kontak '{NamaHapus}' berhasil dihapus")
    else:
        print(f"Kontak '{NamaHapus}' tidak ditemukan")
    
