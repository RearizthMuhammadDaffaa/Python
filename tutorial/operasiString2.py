# operator dalam bentuk methods

## merubah case dari string

# merubah semuanya ke uppercase 
salam = "bro"
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

# merubah semua ke lower case
alay = "aKu MiSkIn"
print('normal = ' + alay)
alay = alay.lower()
print('lower = ' + alay)

## pengecekan dengan menggunakn isX method

# contoh untuk pengecekan lower case
salam = "sis"
apakah_lower = salam.islower()
print(salam + " is lower " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper " + str(apakah_upper))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- huruf dan angka
# isdecimal() <--- angka saja
# isspace() <--- spasi,tab,newline
# istitle() <--- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## ngecek komponen starswith() endswith() <---keren
cek_start = "Gojo Sensei".startswith("Gojo")
print("start = " + str(cek_start))

cek_end = "Gojo Sensei".endswith("Sensei")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku','saya','kamu']
gabung = ' '.join(pisah)
print(pisah)
print(gabung)

gabung = "aku,saya,kamu"
print(gabung.split(','))

# alokasi karakter rjust(),ljust(),center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

center = "center".center(20,"-")
print("'"+center+"'")

# kebalikannya --> strip()
center = center.strip("-")
print("'"+center+"'")

