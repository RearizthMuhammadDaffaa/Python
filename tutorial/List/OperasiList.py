data_angka = [1,2,3,4,5,6,12,3,54,124,2]
print(f"data angka = {data_angka}")

#count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data index
data = ["ucup",'otong',"dudung","ujang"]
print(f"data = {data}")

index_dudung = data.index("dudung")
print(f"index si dudung = {index_dudung}")


# Mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")
print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

#balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = {data_angka} \n{data}")