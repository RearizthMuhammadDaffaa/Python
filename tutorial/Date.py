# Date and time

import datetime as dt

print("silahkan masukan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("tanggal \t:")) 
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah: {tanggal_lahir}")
print(f"hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"umur anda adalah: {umur_tahun} tahun , {umur_bulan_sisa}")
