#Latihan perulangan membuat segitiga

sisi = 5

#dummy variable
# menggunakan for
count = 1

print('awal for')
for i in range(4):
  print("*"*count)
  count += 1

print('akhir for')
# 2.menggunkan while

print('awal While')
count = 1
while True:
  print("*"*count)
  count += 1

  if(count > sisi):
    break

print('akhir While')

# 3.ganjil saja
print('awal While')
count = 1
spasi = int(sisi/2)
while True:
 
  if (count%2):
       #akan print jika genap  
      print(" "*spasi,"+"*count)
      spasi -=1
      count +=1
        # if count == 1:
        #   break
  else:
     #akan kembali ke atas jika ganjil
   
    count += 1
    continue
 

  #akan break jika lebih dari sisi
  if(count > sisi):
    break

print('akhir While\n\n')