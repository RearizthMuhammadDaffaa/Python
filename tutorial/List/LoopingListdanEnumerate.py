# Looping dari list

# for loop
kumpulan_angka = [3,2,4,6,1]

print("for loop")
for angka in kumpulan_angka:
  print(f"angka = {angka}")

peserta = ['ucup','otong','dadang','diding','dudung']

for nama in peserta:
  print(f"nama = {nama}")

# for loop dan range

kumpulan_angka = [10,4,5,20,55]

panjang = len(kumpulan_angka)
print("for loop dan range")
for i in range(panjang):
  print(f"angka = {kumpulan_angka[i]}")

  # while
print("while loop")
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
  print(f"angka = {kumpulan_angka[i]}")
  i += 1

# list comprehension
print("List comprehension")
data = ["ucup",1,2,3,"otong"]
[print(f"data = {i}") for i in data]

# enumerate
print("\nenumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
  print(f"index = {index}, data = {data}")

