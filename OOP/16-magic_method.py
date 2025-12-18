class Mangga:

  # magic method adalah keyword yg sudah 
  #disediakan oleh python contohnya init

  def __init__(self,nama,jumlah):
    self.nama = nama
    self.jumlah = jumlah
  
  def __repr__(self):
    return "Debug - mangga {} dengan jumlah {}".format(self.nama,self.jumlah)
  
  # bedanya str dengan repr adalah 
  # str untuk diproduksi bukan developemtn
  #repr dipakai saat debugging
  def __str__(self):
    return "mangga {} dengan jumlah {}".format(self.nama,self.jumlah)
  
  # add untuk aritmatetika
  def __add__(self,objek):
    return self.jumlah + objek.jumlah
  
  @property
  def __dict__(self):
    return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga('arumanis',10)
belanja2 = Mangga('mana lagai',60)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)