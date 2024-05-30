import numpy as np

# create
data = np.random.rand(2,3,4)
zeros = np.zeros((2,2,2))
full = np.full((2,2,2),7)
ones = np.ones((2,2,2))

print(f"ini adalah random data = \n{data}")
print(f"ini adalah zeros data = \n{zeros}")
print(f"ini adalah full data = \n{full}")
print(f"ini adalah ones data = \n{ones}")

arr = np.array([[1,2,3,4],[1,2,3,4]])
print(f"ini adalah custom data = \n{arr}")
print(type(arr))


# read 
shape = data.shape
size = data.size
types = data.dtype

print(f"ini adalah shape = {shape}")
print(f"ini adalah size = {size}")
print(f"ini adalah types = {types}")

# slicing
arr = data[0]
slicer = data[1:2]
reverse = data[-1]
singleval = data[0][0][0]
print(f"ini adalah update data pertma = {arr}")
print(f"ini adalah slicer = {slicer}")
print(f"ini adalah reverse = {reverse}")
print(f"ini adalah single value = {singleval}")

# update
list1 = np.random.rand(10)
list2 = np.random.rand(10)

# basic math
add = np.add(list1,list2)
sub = np.subtract(list1,list2)
div = np.divide(list1,list2)
mul = np.multiply(list1,list2)
dot = np.dot(list1,list2)

print(f"ini adalah penambahan = {add}")
print(f"ini adalah pengurangan = {sub}")
print(f"ini adalah pembagian = {div}")
print(f"ini adalah perkalian = {mul}")
print(f"ini adalah dot = {dot}")

# stat function
sqrs = np.sqrt(25)
ab = np.abs(-2)
power = np.power(2,7)
log = np.log(25)
exp = np.exp([2,3])
mins = np.min(list1)
max = np.max(list1)
print(f"ini adalah squareroot {sqrs}")
print(f"ini adalah absolute {ab}")
print(f"ini adalah power {power}")
print(f"ini adalah logaritam {log}")
print(f"ini adalah exponetial {exp}")
print(f"ini adalah minimum {mins}")
print(f"ini adalah maximum {max}")

# assigment 
data[0][0][0] = 700
print(data)
#sort
data.sort()
print(data)
#reshape
print(data.shape)
data = data.reshape(2,2,-1)
print(data)

#append
zeroes = np.zeros((8))
print(zeros)
zeroes = np.append(zeroes,[1,2])
print(zeroes)

#insert 
zeroes = np.insert(zeroes,2,1)
print(zeroes)


# delete 
np.delete(data,0,axis=1)
print(data)