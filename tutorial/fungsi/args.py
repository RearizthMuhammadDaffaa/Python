'''*args'''

# memasukan data/argument
def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",100,120])

# kenalan *args

def fungsi(*args):
  nama = args[0]
  tinggi = args[1]
  berat = args[2]
  print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("Daffaa",173,60)