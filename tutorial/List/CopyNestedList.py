data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

# mengambil data dari nested list
data = data_2D[0][0]
print(f"data = {data}")

# address semuanya 
print(f"address asli = {hex(id(data_2D))}")
print(f"address Copy = {hex(id(data_2D_copy))}")

print(f"address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address Copy = {hex(id(data_2D_copy[0]))}")

data_2D[0][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")
#yang bukan list bisa dicopy yang list yang dicopy address nya
# jadi disebut shallow copy untuk mengatasi bisa menggunakan deep copy

#kita gunakan deep copy

from copy import deepcopy 
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print(f"address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address Copy = {hex(id(data_2D_deepcopy[0]))}")

