data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,data_list_biasa,6,7]

print(f"list 2D = {list_2D}")

# contoh penggunaan

pesera_0 = ['Ucup',25,"Laki-Laki"]
pesera_1 = ['Otong',10,"Laki-Laki"]
pesera_2 = ['Dedeh',50,"Wanita"]

list_peserta = [pesera_0,pesera_1,pesera_2]

print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
  print(f"Nama\t: {peserta[0]}")
  print(f"Umur\t: {peserta[1]}")
  print(f"Kelamin\t: {peserta[2]}\n")


# dengan reference
list_copy = list_peserta.copy()
print(f"Peserta = {list_copy}")
pesera_0[0] = "Michael"
print(f"Peserta = {list_copy}")
print(f"Peserta = {list_peserta}")

