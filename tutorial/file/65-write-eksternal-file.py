import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR,"data_1.txt")
file_path_3 = os.path.join(BASE_DIR,"data_2.txt")

# 1.mode write
# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya



with open(file_path,'w',encoding="utf-8") as file:
  file.write("ucup surucup")

with open(file_path,'w',encoding="utf-8") as file:
  file.write("mantap")
with open(file_path,'w',encoding="utf-8") as file:
  file.write("overwrite")


# 2.mode append
with open(file_path,'w',encoding="utf-8") as file:
  file.write("ucup surucup\n")

with open(file_path,'a',encoding="utf-8") as file:
  file.write("mantap\n")

with open(file_path,'a',encoding="utf-8") as file:
  file.write("tambah dengan append")

# 3.mode r+
with open("data_3.txt",'w',encoding="utf-8") as file:
  file.write("ini adalah data ke3\n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
  file.write("baris 1 \n")
  file.write("baris 2 \n")
  file.write("baris 3 \n")
   

with open("data_3.txt",'r+',encoding="utf-8") as file:
  data = file.read()
  print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
  file.write("otojng surotng") #menimpa isi text sesuai dengan panjang data