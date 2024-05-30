## ---LIST ---

# kumpulan data numvbers
data_angka = [1,2,3]
print(data_angka)


# Kumpulan data string
data_string = ["Rearizth","Muhammad","Daffaa"]
print(data_string)

#Kumpulan Boolean
data_bool = [True,False,True,False]
print(data_bool)

#Kumpulan campuran
data_campuran = [1,"Gehu",2,"Bala-bala","ucup",True]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10) #range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list dengan for loop,list comphrehensif
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)

#membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if)