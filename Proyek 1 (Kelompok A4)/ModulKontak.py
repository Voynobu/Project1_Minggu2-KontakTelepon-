
def DaftarKontak():
    Buka = open("daftarkontak.txt","r")
    print(Buka.read())
    Buka.close()

def TambahKontak(NamaNew, NomorNew):
    template = f"\n Nama : {NamaNew}, Nomor : {NomorNew}"
    Buka = open("daftarkontak.txt","a")
    Buka.write(template)
