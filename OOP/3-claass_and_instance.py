class Hero: #template
  #class variable
  jumlah = 0

  def __init__(self,inputName,inputHealth,inputPower,inputArmor):
    #intance variable 
    self.name = inputName
    self.health = inputHealth
    self.power = inputPower
    self.armor = inputArmor
    Hero.jumlah += 1
    print("Membuat hero dengan nama " + inputName)



hero1 = Hero("sniper",100,10,4)
print(Hero.jumlah)
hero2 = Hero("Mirana",100,13,1)
print(Hero.jumlah)
hero3 = Hero("Ucup",1000,100,0)
print(Hero.jumlah)

print(Hero.__dict__)



