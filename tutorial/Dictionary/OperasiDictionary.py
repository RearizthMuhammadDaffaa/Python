# operator untuk dictionary
data_dict = {
  "cup":'ucup',
  "tong":'otong surotong',
  "dung":'dudung surudung'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjanf dari dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di dictionary: {CHECKKEY}")

# mengakses value {read} dengan megguanakn get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get('kiss',"key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "Ucup si kntl"
print(data_dict.get("cup"))

# menambah data
data_dict["sep"] = "asep si kehed"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"Daffaa":"daffaa mnata"}) # kalau tidak ada di add saja
print(data_dict)

# delete data dictionary
del data_dict['Daffaa']
print(data_dict)
