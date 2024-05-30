# wifth and Multiline

# data

data_nama = "Rearizth Daffaa"
data_umur = 21
data_tinggi = 173
data_nomor_sepatu = 42

# String
data_string = f"nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi} nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter ,newline,\n)
data_string = f"nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi} \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama   = {data_nama:>10}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)