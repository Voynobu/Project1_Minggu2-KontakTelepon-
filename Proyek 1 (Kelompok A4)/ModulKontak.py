import os

fileKontak = "daftarkontak.txt"

# Rangga Muhamad fajar
def TambahKontak(Nama, Nomor):
    template = f"\n Nama : {Nama}, Nomor : {Nomor}"
    Buka = open("daftarkontak.txt","a")
    Buka.write(template)
    
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
    
    
