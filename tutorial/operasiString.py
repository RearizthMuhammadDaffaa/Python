# operasi dan manipulasi String

# 1.menyambung String(concatenate)
nama_pertama = "rearizth "
nama_tengah = "Muhammad "
nama_akhir = "Daffaa"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

# 2 Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari nama lengkap "+ str(panjang))

# 3 operator string

# mengecek apakah ada komponen karakter atau string di string
d = 'd'
status = d in nama_lengkap
print("string " + d + " ada di "+ str(status))

x = 'x'
status = d not in nama_lengkap
print("string " + d + " tidak ada di "+ str(status))

# mengulang string
print("wk"*2)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-[0,3]: " + nama_lengkap[0:3])
print("index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil " + min(nama_lengkap))
print("paling besar " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4.operator dalam bentuk method
data = "otong surotong korortong"
jumlah = data.count("o")
print('jumlah o pada data ' + data + "= " + str(jumlah))

