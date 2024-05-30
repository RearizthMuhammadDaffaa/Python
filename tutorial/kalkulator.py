print("kalkulator sederhana")
angka_1 = int(input("masukan nilai pertama: "))
angka_2 = int(input("masukan nilai kedua: "))
operator = input("masukan operator = ")

if operator == "+":
            print(f"hasilnya ialah: {angka_1 + angka_2}")
elif operator == "-":
            print(f"hasilnya ialah: {angka_1 - angka_2}")
elif operator == "x":
            print(f"hasilnya ialah: {angka_1 * angka_2}") 
elif operator == "/":
            print(f"hasilnya ialah: {angka_1 / angka_2}")
else:
        print("input yang anda masukkan salah")
print("terima kasih telah menggunakan kalkulator")