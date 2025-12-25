from . import Operasi

def delete_console():
  read_console()
  while(True):
    print("silahkan pilih no buku yg akan didelete")
    no_buku = int(input("Nomor buku: "))
    data_buku = Operasi.read(index=no_buku)
    
    if data_buku:
      data_break = data_buku.split(',')
      pk = data_break[0]
      data_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4][:-1]
      
      
      #data yang ingin diubah
      print("\n" + "="*100)
      print("Data apa yang ingin anda deleete")
      print(f"1. Judul\t {judul:.40}")
      print(f"2. Penulis\t {penulis:.40}")
      print(f"3. Tahun\t {tahun:4}")
      is_done = input("Yakin akan dihapus  (y/n)")
      if is_done == "y" or is_done == "Y":
        Operasi.delete(no_buku)
        break
    else:
      print("nomor tidak valid")
  print("Data berhasil dihapus")
        
    
    

def update_console():
  read_console()
  while(True):
    print("Data yang ingin anda hapus")
    no_buku = int(input("Nomor buku: "))
    data_buku = Operasi.read(index=no_buku)
    
    if data_buku:
      break
    else:
      print("nomor tidak valid")
  
  data_break = data_buku.split(',')
  pk = data_break[0]
  data_add = data_break[1]
  penulis = data_break[2]
  judul = data_break[3]
  tahun = data_break[4][:-1]
  
  while(True):
    #data yang ingin diubah
    print("\n" + "="*100)
    print("Data apa yang ingin anda ubah")
    print(f"1. Judul\t {judul:.40}")
    print(f"2. Penulis\t {penulis:.40}")
    print(f"3. Tahun\t {tahun:4}")
    
    #memilih mode untuk update
    user_option = input("Pilih data [1,2,3]")
    print("\n" + "="*100)
    match user_option:
      case "1":judul = input("Judul\t: ")
      case "2":penulis = input("penulis\t: ")
      case "3":
        while(True):
          try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun harus angka,silahkan masukan tahun lagi')
          except : 
            print('Tahun harus angka,silahkan masukan tahun lagi')
      case _ : print("index tidak cocok")
    
    print("data baru anda")
    print(f"1. Judul\t {judul:.40}")
    print(f"2. Penulis\t {penulis:.40}")
    print(f"3. Tahun\t {tahun:4}")
    is_done = input("Apakah data sesuai  (y/n)")
    if is_done == "y" or is_done == "Y":
      break
    
  Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

def create_console():
  print("\n\n" + "="*100)
  print("SIlahkan tambah data buku\n")
  penulis = input("Penulis\t: ")
  judul = input("Judul\t: ")
  while(True):
      try:
        tahun = int(input("Tahun\t: "))
        if len(str(tahun)) == 4:
            break
        else:
            print('Tahun harus angka,silahkan masukan tahun lagi')
      except : 
        print('Tahun harus angka,silahkan masukan tahun lagi')
   
  Operasi.create(tahun,judul,penulis)
  print("\n berikut adalah data baru anda")
  read_console()
   
    


def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # header
    print("\n" + "m"*100)
    print(f"{index:4}| {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    print("data")
    
    #data
    for index,data in enumerate(data_file):
      data_break = data.split(",")
      pk = data_break[0]
      date_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4]
      print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
    
    #footer
    print("m"*100 + "\n")