# program list buku


list_buku = []

while True:
    print("Masukan data buku")
    judul = input("masukan judul buku\t:")
    penulis = input("masukan nama penulis\t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
  
    print("no.| judul| penulis")
    print("\n\n","="*10,"data buku","="*10)
    for index,buku in enumerate(list_buku):
          print(f"{index+1} |{buku[0]}|{buku[1]}")
    
    print("\n\n","="*20)
    isLanjut = input("apakah di lanjutkan? (y/n)")

    if isLanjut == "n":
         break

print("Program selesai")