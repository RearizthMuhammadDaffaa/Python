class Hero:

  def __init__(self,name,health,attackPower,armorNumber):
    self.name = name
    self.health = health
    self.attackPower = attackPower
    self.armorNumber = armorNumber

  def serang(self, Hero):
    print(self.name + ' Menyerang ' + Hero.name)
    Hero.diserang(self,self.attackPower)
  
  def diserang(self,Hero,attackPower_lawan):
    print(self.name + ' Diserang ' + Hero.name)
    attackDiterima = attackPower_lawan / self.armorNumber
    print('serangan terasa : ' + str(attackDiterima))
    self.health -= attackDiterima
    print('Health tersisa : ' +str(self.health))


sniper = Hero('Sniper' , 100,10,5)
rikimaru = Hero('rikimaru' ,100,20,10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)


