
def TambahKontak(NamaNew, NomorNew):
    template = f"\n Nama : {NamaNew}, Nomor : {NomorNew}"
    Buka = open("daftarkontak.txt","a")
    Buka.write(template)

def TampilKontak():
    Buka = open("daftarkontak.txt", "r")
    print(Buka.read())
    Buka.close()
    
