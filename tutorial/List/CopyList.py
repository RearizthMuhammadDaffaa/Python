# teknik menduplikat list
a = ["ucup","otong","dudung"]
b = a

#address dari kedua list 
print(f"addtess a = {hex(id(a))}")
print(f"addtess b = {hex(id(b))}")


# menduplikat list 
print("membuat list c dengan a.copy()")
c = a.copy()
print(f"addtess a = {hex(id(a))}")
print(f"addtess b = {hex(id(b))}")
print(f"addtess c = {hex(id(c))}")