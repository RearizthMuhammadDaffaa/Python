# class abstract
# tidak bisa membuat objek dari abstract class
# untuk abstrack class,class yang inheritance atau subclass
#harus mengimplementasikan method yang abstrack di superclass
# jadi abstract class adalah class yang behavior nya sama dan
#harus diimplemetnasikan methdnya ke semua subclass
# abc = abstract base class
from abc import ABC,abstractmethod

class Button(ABC):

  @abstractmethod
  def click(self):
    print("button click")

class PushButton(Button):

  def click(self):
    print("push button click")

tombol1 = PushButton()

tombol1.click()
help(tombol1)