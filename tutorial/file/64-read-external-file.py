import os
## tutorial membaca file ekesternal file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR,"data.txt")


print(3*"=", " Membaca file txt ", 3*"=")
file = open(file_path,mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
# print(file.read())

# baca perbaris
print(file.readline(),end="") #baca baris pertama
print(file.readline(),end="") # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose: {file.closed}")

file.close()
print(f"apakah file sudah diclose: {file.closed}")


## salah satu teknik membuka file di python

print('\n',3*"=", " Membaca file txt dengan with ", 3*"=")

# yang with jika keluar dari fungsi with maka 
#akan otomatis di close
with open(file_path,mode="r") as file:
  content = file.readline()
  print(content,end="")

