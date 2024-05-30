# latihan logika dan komparasi

# membuat gabungan area rentang dari sebuah angka 

# ++++++3------10++++++++

inputUser = float(input("Masukkan Angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10 "))

# +++++++3-------------
# Memeriksa angka kurang dari 36
isKurangDari = (inputUser < 3 )
print(isKurangDari)


# -----------------10++++++++++++++
# Memeriksa apakah lebih dari 10
isLebihDari = (inputUser > 10)
print(isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ",isCorrect)

print("=========akhir or=========")

# ------3++++++++10-------
# kasus irisan
print('\n',10*'=','\n')
inputUser = float(input("Masukkan Angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10 "))


# ---------3+++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print(isLebihDari)


# ++++++++++++++++++++10-----------
isKurangDari = inputUser < 10
print('kurang dari 10 = ',isKurangDari)


isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ",isCorrect)

# pr Masukkan angka
# --------0++++++++5-------8+++++++++11---------
# ++++++++0--------5+++++++8---------11+++++++++


print('\n',10*'=','\n')
inputUser = float(input("Masukkan Angka: "))
isLebihDari = inputUser < 11 and inputUser > 8
isKurangDari = inputUser < 5 and inputUser > 0

isCorrect = isKurangDari or isLebihDari

print('isCorrect adalah = ', isCorrect)



print('\n',10*'=','\n')
inputUser = float(input("Masukkan Angka: "))
isLebihDari = inputUser < 0 or inputUser > 11
isKurangDari = inputUser > 5 and inputUser < 8

isCorrect = isKurangDari or isLebihDari

print('isCorrect = ',isCorrect)

