import datetime

mahasiswa1 = {
  'nama':'ucup surucup',
  'nim':'199022012',
  'sks_lulus':120,
  'beasiswa':False,
  'lahir':datetime.datetime(2000,2,10)
}

mahasiswa2 = {
  'nama':'otong surotong',
  'nim':'199022012',
  'sks_lulus':140,
  'beasiswa':True,
  'lahir':datetime.datetime(2002,7,7)
}

mahasiswa3 = {
  'nama':'Asep',
  'nim':'199022012',
  'sks_lulus':100,
  'beasiswa':False,
  'lahir':datetime.datetime(2002,2,12)
}

data_mahasiswa = {
  'MAH001':mahasiswa1,
  'MAH002':mahasiswa2,
  'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {"beasiswa":<9} {"lahir":<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
  KEY = mahasiswa
  NAMA = data_mahasiswa[KEY]['nama']
  NIM = data_mahasiswa[KEY]['nim']
  SKS = data_mahasiswa[KEY]['sks_lulus']
  BEASISWA = data_mahasiswa[KEY]['beasiswa']
  LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
  print(f"{mahasiswa:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

