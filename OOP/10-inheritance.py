class Hero:

  def __init__(self,name,heatlh):
    self.name = name
    self.health = heatlh


class Hero_intelligent(Hero):
  pass

class Hero_strength(Hero):
  pass

lina = Hero('lina',100)
teachies = Hero_intelligent('teachies',100)
axe = Hero_strength('axe',200)

print(lina.name)
print(teachies.name)
print(axe.name)
    