# format string


# contoh generic
# String
nama = "daffaa"
format_str = f"hello {nama}"

print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2002.2
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan ordo ribuan
angka = 200000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2002.2232323
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2002.2232323
format_str = f"desimal = {angka:09.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.22
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.1f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga * jumlah:,}"
print(format_string)

# format angka lain {binary,octal,hexadecimal}
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
