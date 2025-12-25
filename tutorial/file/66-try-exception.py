# execption akan terjadi saat program
# mengalami error saat runtime

from math import nan

# contoh sederhan untuk menangkap exeption

# input_user = int(input("Masukan angka: "))
# hasil = 0

# try:
#   hasil = 10/input_user
# except:
#   print("input tidak boleh 0")

# print(f"hasil = {hasil}")

#contoh diaplaikasi

while(True):
  angka = int(input("masukan angka pembagi :"))
  try:
    hasil = 10/angka
    print(f"hasil = {hasil}")
    is_done = input("lanjutkan atau tidak y/n")
    if is_done == "n":
      break
  except:
    print("pembagi nol,silahkan masukkan input lagi")
  
print("ini adalah akhir adalah program")

# contoh aplikasi untuk membuat file data.txt
while(True):
  try:
    with open("data_2.txt",'r') as file :
      print(file.read())
      break
  except:
    print("file data tidak ditemukan,membuat file baru")
    with open("data_2.txt",'w',encoding="utf-8") as file:
      file.write("data baru")
      break
