# Method resolution order adalah urutan suatu 
# objek didalm multiple inheritance

class A:

  def show(self):
    print("ini adalah A")

class B:
  def show(self):
    print("ini adalah B")

class C(B,A): # Urutannya adalah C>B>A
  pass

objek = C()
objek.show()