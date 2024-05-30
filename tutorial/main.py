#  latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("/nPROGRAM KONVERSI TEMPERATURE/n")

celcius = float(input("Masukan suhu dalam celcius :"))
print('suhu adalah = ', celcius , "Celcius")

# reamur
# (4/5) *C
reamur = (4/5) * celcius
print('suhu dalam reamur = ', reamur , "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) +32
print('suhu dalam Fahrenhei = ', fahrenheit , "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print('suhu dalam kelvin = ', kelvin , "kelvin")

a = (fahrenheit -32) * (5/9) + 273
print('suhu dalam fahrenheit ke kelvin = ', a , "kelvin")

b = (kelvin - 273) * (9/5) + 32
print('suhu dalam kelvin ke fahrenheit = ', b , "fahrenheit")
