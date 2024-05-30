# copy dict

teman_teman = {
  "cup":"ucup surucup",
  "tong":"otong surotong",
  "dung":"dudung surudung",
  "sep" : "asep si aspe"
}

friends = teman_teman.copy()
print(f"teman-teman : {teman_teman}")
print(f"friends : {friends}")

# pop dictionary
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary
dataTerakhir = friends.popitem()
print(f"data Terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")