#__main__ adalah top level code enviroment

# __name__ == __main__ akan terjadi jika ada di program utama


#__name__ == "__main__"
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ fungsi pada file program dieksternal
import testFungsi

# contoh penggunaan __main__

#deklarasi
def fungsi_tambah(a:int,b:int)->int:
  return a+b

if __name__ == "__main__":
  angka1 = 5
  angka2 = 10
  hasil = fungsi_tambah(angka1,angka2)
  print(hasil)



## import package
import package