'''**kwargs'''

def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(**kwargs):
  nama = kwargs["nama"]
  tinggi = kwargs['tinggi']
  berat = kwargs['berat']
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup",tinggi=170,berat=40)

# studi kasus

def math(*args,**kwargs):
  output = 0
  if kwargs["option"] == "tambah":
    for angka in args:
      output += angka
  elif kwargs["option"] == "kali":
    output = 1
    for angka in args:
      output *= angka
  else:
    print("tidak ada perkalian")
  return output


hasil = math(1,2,3,4,5,6,option="tambah")
hasil_kali = math(1,2,3,4,5,6,option="kali")

print(f"hasil jumlah = {hasil}")
print(f"hasil kali = {hasil_kali}")