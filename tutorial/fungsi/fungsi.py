"""
  Latihan fungsi
"""

import os

# program menghitung luas dan keliling persegi panjang

# Membuat header program

# os.system("cls")
# print(f"{'Program menghitung Luas':^40}")
# print(f"{'Dan keliling Persegi panjang':^40}")
# print(f"{'-'*40:^40}")

# # mengambil Input user
# LEBAR =  int(input("Masukan Nilai Lebar: "))
# PANJANG = int(input("Masukan Nilai Panjang: "))

# # Program menghitung luas 
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG + LEBAR)

# # Tampilkan hasilnya
# print(f"hasil perhitungan luas : {LUAS}")
# print(f"hasil perhitungan keliling : {KELILING}")

def header():
  os.system("cls")
  print(f"{'Program menghitung Luas':^40}")
  print(f"{'Dan keliling Persegi panjang':^40}")
  print(f"{'-'*40:^40}")

def input_user():
    # mengambil Input user
  lebar =  int(input("Masukan Nilai Lebar: "))
  panjang = int(input("Masukan Nilai Panjang: "))
  return lebar,panjang


def hitung_luas(lebar,panjang):
  return lebar * panjang

def hitung_keliling(lebar,panjang):
  return 2*(lebar + panjang)

def display(message,value):
  print(f"{message} = {value}")


while True:
  header()
  LEBAR,PANJANG = input_user()
  LUAS = hitung_luas(LEBAR,PANJANG)
  KELILING = hitung_keliling(LEBAR,PANJANG)

  display("luas",LUAS)
  display("keliling",PANJANG)

  isContinue = input("Apkah lanjut (y/n)")
  if isContinue == "n":
    break

print("program selesai terima kasih")