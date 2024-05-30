## operaso

data = ["ucup","otong","dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0 ) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

data_ucup = data[-3]
print(f"ini adalah ucup = {data_ucup}")


#mengambil jumlah data dari list
panjang_data = len(data)
print(f"ini adalah panjang data = {panjang_data}")

## Manipulasi data list

# Menambahkan Item pada list
print(f"ini data sebelum ditambah = {data}")
data.insert(1,"Asep")
print(f"data sesudah ditambah = {data}")

# Menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi = {data}")

# Menambahkan List dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

#Merubah data 
#ubah data-2 menjadi michael
data[2] = "michael"
print(f"data rubah = {data}")

#meremove data
data.remove("Ujang")
print(f"data remove = {data}")

# Meremove data paling belakang
data.pop()
print(f"data akhir = {data}")
